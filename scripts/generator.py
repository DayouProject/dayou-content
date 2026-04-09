from __future__ import annotations

import argparse
import json
import os
import random
import re
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Any
from urllib import request
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = ROOT / "config.yaml"

WEEKDAY_INDEX = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

ANGLE_LIBRARY = [
    "what to do when life feels uncertain",
    "how to stop forcing timing",
    "why ambition needs inner steadiness",
    "how to read mixed signals in relationships",
    "how to protect your energy without hardening your heart",
    "what ancient wisdom says about burnout",
    "how to tell the difference between intuition and anxiety",
    "why change feels scary right before clarity appears",
    "how to stay calm when other people are chaotic",
    "why softness can be a real strategy",
]


class LLMError(RuntimeError):
    """Raised when the LLM provider returns an invalid response."""


@dataclass(slots=True)
class CorpusEntry:
    source_id: str
    source_title: str
    language: str
    path: str
    title: str
    body: str

    @property
    def key(self) -> str:
        return f"{self.source_id}:{Path(self.path).stem}"


@dataclass(slots=True)
class GeneratedScript:
    script_id: str
    week_label: str
    title: str
    source_id: str
    source_title: str
    source_path: str
    source_excerpt: str
    angle: str
    scheduled_for: str
    timezone: str
    hook: str
    body_points: list[str]
    cta: str
    caption: str
    hashtags: list[str]
    visual_direction: str
    duration_seconds: int
    script_path: str = ""
    generation_mode: str = "llm"
    video: dict[str, Any] = field(default_factory=dict)
    publish: dict[str, Any] = field(default_factory=dict)


def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_week_start(value: date | None) -> date:
    if value is None:
        today = datetime.now().date()
    else:
        today = value
    return today - timedelta(days=today.weekday())


def strip_code_fences(text: str) -> str:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    return cleaned.strip()


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return normalized or "script"


def read_source_payload(path: Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8").strip()
    parts = raw.split("--- Notes ---", maxsplit=1)
    primary = parts[0].strip()
    lines = [line.strip() for line in primary.splitlines() if line.strip()]
    title = lines[0] if lines else path.stem
    body = "\n".join(lines[1:]).strip() or primary
    return title, body


class OpenAICompatibleLLM:
    """Tiny REST client for OpenAI-compatible chat completions."""

    def __init__(self, config: dict[str, Any]) -> None:
        api_key_env = config["api_key_env"]
        self.api_key = os.getenv(api_key_env, "")
        self.base_url = config["base_url"].rstrip("/")
        self.endpoint = config.get("endpoint", "/chat/completions")
        self.model = config["model"]
        self.temperature = float(config.get("temperature", 0.8))
        self.max_tokens = int(config.get("max_tokens", 1200))
        self.timeout_seconds = int(config.get("timeout_seconds", 90))
        self.json_mode = bool(config.get("json_mode", True))

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key)

    def generate_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        if not self.api_key:
            raise LLMError("Missing LLM API key in environment.")

        payload: dict[str, Any] = {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        if self.json_mode:
            payload["response_format"] = {"type": "json_object"}

        payload_bytes = json.dumps(payload).encode("utf-8")
        http_request = request.Request(
            url=f"{self.base_url}{self.endpoint}",
            data=payload_bytes,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
            data = json.loads(response.read().decode("utf-8"))
        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as exc:
            raise LLMError(f"Unexpected LLM response shape: {data}") from exc

        if isinstance(content, list):
            text = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        else:
            text = str(content)

        try:
            return json.loads(strip_code_fences(text))
        except json.JSONDecodeError as exc:
            raise LLMError(f"LLM did not return valid JSON: {text}") from exc


class ScriptGenerator:
    """Generates a weekly batch of Dayou avatar scripts."""

    def __init__(self, config: dict[str, Any], root: Path = ROOT) -> None:
        self.config = config
        self.root = root
        self.output_root = root / config["project"]["output_root"]
        self.template = (self.root / "scripts" / "templates" / "avatar_script.md").read_text(encoding="utf-8")
        self.translation_rules = (self.root / "CULTURAL_TRANSLATION.md").read_text(encoding="utf-8")
        self.persona = config["persona"]
        self.llm = OpenAICompatibleLLM(config["llm"])

    def load_corpus(self) -> list[CorpusEntry]:
        entries: list[CorpusEntry] = []
        for source in self.config["corpus"]["sources"]:
            source_dir = self.root / source["path"]
            for file_path in sorted(source_dir.glob("*.txt")):
                title, body = read_source_payload(file_path)
                entries.append(
                    CorpusEntry(
                        source_id=source["id"],
                        source_title=source["title"],
                        language=source["language"],
                        path=str(file_path.relative_to(self.root)),
                        title=title,
                        body=body,
                    )
                )
        if not entries:
            raise FileNotFoundError("No corpus files found under configured source paths.")
        return entries

    def build_week_schedule(self, week_start: date, count: int) -> list[datetime]:
        schedule = self.config["publish"]["schedule"]
        timezone_name = schedule["timezone"]
        zone = ZoneInfo(timezone_name)
        slots = schedule["slots"]

        resolved: list[datetime] = []
        current_week_start = normalize_week_start(week_start)
        sorted_slots = sorted(slots, key=lambda slot: (WEEKDAY_INDEX[slot["weekday"]], slot["time"]))

        while len(resolved) < count:
            for slot in sorted_slots:
                day_offset = WEEKDAY_INDEX[slot["weekday"]]
                hour, minute = (int(piece) for piece in slot["time"].split(":", maxsplit=1))
                scheduled_date = current_week_start + timedelta(days=day_offset)
                resolved.append(datetime.combine(scheduled_date, time(hour, minute), tzinfo=zone))
                if len(resolved) == count:
                    break
            current_week_start += timedelta(days=7)
        return resolved

    def weighted_source_cycle(self) -> list[str]:
        weighted: list[str] = []
        for source in self.config["corpus"]["sources"]:
            weighted.extend([source["id"]] * int(source.get("weight", 1)))
        return weighted

    def plan_batch(self, week_start: date, count: int) -> list[tuple[CorpusEntry, datetime, str]]:
        corpus = self.load_corpus()
        schedule = self.build_week_schedule(week_start, count)
        by_source: dict[str, list[CorpusEntry]] = {}
        for entry in corpus:
            by_source.setdefault(entry.source_id, []).append(entry)

        weighted_sources = self.weighted_source_cycle()
        seed = int(normalize_week_start(week_start).strftime("%G%V"))
        chooser = random.Random(seed)

        plan: list[tuple[CorpusEntry, datetime, str]] = []
        for index in range(count):
            source_id = weighted_sources[index % len(weighted_sources)]
            entry = chooser.choice(by_source[source_id])
            angle = ANGLE_LIBRARY[index % len(ANGLE_LIBRARY)]
            plan.append((entry, schedule[index], angle))
        return plan

    def build_system_prompt(self) -> str:
        return (
            "You write short-form avatar scripts for Dayou, a Chinese metaphysics AI brand. "
            "Write in natural English for overseas TikTok and Instagram audiences. "
            "Keep the voice emotionally precise, culturally respectful, and practical. "
            "Return valid JSON only."
        )

    def build_user_prompt(self, entry: CorpusEntry, scheduled_for: datetime, angle: str) -> str:
        return f"""
Persona:
{json.dumps(self.persona, ensure_ascii=False, indent=2)}

Schedule:
- Publish at: {scheduled_for.isoformat()}

Source:
- Source ID: {entry.source_id}
- Source Title: {entry.source_title}
- File: {entry.path}
- Text Title: {entry.title}
- Language: {entry.language}
- Focus Angle: {angle}

Source Excerpt:
{entry.body}

Template Contract:
{self.template}

Cultural Translation Rules:
{self.translation_rules}

Create one short vertical-video script and return JSON with exactly these keys:
- title
- hook
- body_points
- cta
- caption
- hashtags
- visual_direction
- duration_seconds

Constraints:
- `body_points` must be an array of 3 strings or fewer.
- Use English as the primary language.
- If the Chinese phrase helps, include only one short quoted line.
- Keep the spoken script under 900 characters total.
- Keep the CTA soft.
- Hashtags should be useful, not spammy.
""".strip()

    def fallback_script(self, entry: CorpusEntry, scheduled_for: datetime, angle: str, week_label: str, index: int) -> GeneratedScript:
        body_points = [
            f"This line points to {angle}, but through pattern instead of pressure.",
            "The message is simple: stop trying to control every outcome and watch what the situation is already revealing.",
            "Use the teaching as a mirror for your next decision, not as a superstition or fixed prophecy.",
        ]
        title = f"{entry.source_title.split('/')[0].strip()}: {angle.capitalize()}"
        quote_line = entry.body.splitlines()[0][:120]
        caption = (
            f"{quote_line}\n\n"
            f"A short Dayou reading on {angle}. "
            "Save this if you need a calmer way to read change."
        )
        return GeneratedScript(
            script_id=f"{week_label}-{index:02d}",
            week_label=week_label,
            title=title,
            source_id=entry.source_id,
            source_title=entry.source_title,
            source_path=entry.path,
            source_excerpt=entry.body[:300],
            angle=angle,
            scheduled_for=scheduled_for.isoformat(),
            timezone=scheduled_for.tzinfo.key if scheduled_for.tzinfo else "UTC",
            hook=f"If life feels unclear right now, this ancient line is telling you where to look.",
            body_points=body_points,
            cta=self.persona["cta"],
            caption=caption,
            hashtags=["#dayou", "#easternwisdom", "#iching", "#taoism", "#selfreflection"],
            visual_direction="Centered avatar, warm neutral background, calm subtitles, one highlighted keyword per beat.",
            duration_seconds=45,
            generation_mode="fallback",
        )

    def generate_script(
        self,
        entry: CorpusEntry,
        scheduled_for: datetime,
        angle: str,
        week_label: str,
        index: int,
        dry_run: bool,
    ) -> GeneratedScript:
        if dry_run or not self.llm.is_configured:
            return self.fallback_script(entry, scheduled_for, angle=angle, week_label=week_label, index=index)

        payload = self.llm.generate_json(
            system_prompt=self.build_system_prompt(),
            user_prompt=self.build_user_prompt(entry, scheduled_for, angle),
        )

        body_points = [str(item).strip() for item in payload.get("body_points", []) if str(item).strip()]
        if not body_points:
            raise LLMError("LLM response missing body_points.")

        hashtags = [str(item).strip() for item in payload.get("hashtags", []) if str(item).strip()]
        return GeneratedScript(
            script_id=f"{week_label}-{index:02d}",
            week_label=week_label,
            title=str(payload["title"]).strip(),
            source_id=entry.source_id,
            source_title=entry.source_title,
            source_path=entry.path,
            source_excerpt=entry.body[:300],
            angle=angle,
            scheduled_for=scheduled_for.isoformat(),
            timezone=scheduled_for.tzinfo.key if scheduled_for.tzinfo else "UTC",
            hook=str(payload["hook"]).strip(),
            body_points=body_points[:3],
            cta=str(payload["cta"]).strip(),
            caption=str(payload["caption"]).strip(),
            hashtags=hashtags,
            visual_direction=str(payload.get("visual_direction", "")).strip(),
            duration_seconds=int(payload.get("duration_seconds", 45)),
            generation_mode="llm",
        )

    def render_markdown(self, script: GeneratedScript) -> str:
        body = "\n".join(f"{idx}. {point}" for idx, point in enumerate(script.body_points, start=1))
        hashtags = " ".join(script.hashtags)
        return f"""# {script.title}

Source: {script.source_title}
Source file: {script.source_path}
Angle: {script.angle}
Scheduled for: {script.scheduled_for}
Generation mode: {script.generation_mode}

## HOOK
{script.hook}

## BODY
{body}

## CTA
{script.cta}

## CAPTION
{script.caption}

{hashtags}

## VISUAL_DIRECTION
{script.visual_direction}
""".strip() + "\n"

    def save_batch(self, scripts: list[GeneratedScript], week_start: date) -> Path:
        week_label = normalize_week_start(week_start).strftime("%G-W%V")
        batch_dir = self.output_root / "scripts" / week_label
        scripts_dir = batch_dir / "scripts"
        scripts_dir.mkdir(parents=True, exist_ok=True)

        for index, script in enumerate(scripts, start=1):
            file_name = f"{index:02d}_{slugify(script.title)[:50]}.md"
            output_path = scripts_dir / file_name
            output_path.write_text(self.render_markdown(script), encoding="utf-8")
            script.script_path = str(output_path.relative_to(self.root))

        manifest = {
            "project": self.config["project"]["name"],
            "generated_at": datetime.now().isoformat(),
            "week_label": week_label,
            "week_start": normalize_week_start(week_start).isoformat(),
            "timezone": self.config["publish"]["schedule"]["timezone"],
            "scripts": [asdict(script) for script in scripts],
        }
        manifest_path = batch_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        return manifest_path

    def generate_week(self, week_start: date | None = None, count: int | None = None, dry_run: bool = False) -> Path:
        resolved_week_start = normalize_week_start(week_start)
        count = count or int(self.config["corpus"].get("weekly_scripts", 7))
        plan = self.plan_batch(resolved_week_start, count)
        week_label = resolved_week_start.strftime("%G-W%V")
        scripts: list[GeneratedScript] = []

        for index, (entry, scheduled_for, angle) in enumerate(plan, start=1):
            script = self.generate_script(
                entry=entry,
                scheduled_for=scheduled_for,
                angle=angle,
                week_label=week_label,
                index=index,
                dry_run=dry_run,
            )
            scripts.append(script)

        return self.save_batch(scripts, resolved_week_start)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Dayou weekly avatar scripts.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.yaml")
    parser.add_argument("--week-of", help="Any date inside the target week, format YYYY-MM-DD")
    parser.add_argument("--count", type=int, default=7, help="Number of scripts to generate")
    parser.add_argument("--dry-run", action="store_true", help="Skip live LLM calls and use fallback copy")
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    config_path = Path(args.config).resolve()
    config = load_config(config_path)
    week_of = date.fromisoformat(args.week_of) if args.week_of else None

    generator = ScriptGenerator(config=config, root=config_path.parent)
    manifest_path = generator.generate_week(week_start=week_of, count=args.count, dry_run=args.dry_run)
    print(f"Weekly manifest written to {manifest_path}")


if __name__ == "__main__":
    main()
