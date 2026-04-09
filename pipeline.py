from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

from publish.scheduler import N8NPublisher
from scripts.generator import ScriptGenerator
from video.heygen_client import HeyGenClient, HeyGenError

ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH = ROOT / "config.yaml"


def load_config(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def resolve_manifest_path(config: dict[str, Any], explicit_path: str | None = None) -> Path:
    if explicit_path:
        return Path(explicit_path).resolve()

    script_root = ROOT / config["project"]["output_root"] / "scripts"
    manifests = sorted(script_root.glob("*/manifest.json"), key=lambda item: item.stat().st_mtime, reverse=True)
    if not manifests:
        raise FileNotFoundError("No manifest found. Run `python3 pipeline.py generate` first.")
    return manifests[0]


def run_generate(config_path: Path, week_of: date | None, count: int, dry_run: bool) -> Path:
    generator = ScriptGenerator(config=load_config(config_path), root=config_path.parent)
    manifest_path = generator.generate_week(week_start=week_of, count=count, dry_run=dry_run)
    print(f"Generated scripts manifest: {manifest_path}")
    return manifest_path


def run_video(config: dict[str, Any], manifest_path: Path, wait: bool, dry_run: bool, timeout_seconds: int) -> Path:
    manifest = load_manifest(manifest_path)
    client = HeyGenClient(config["heygen"])

    for script in manifest["scripts"]:
        existing_status = str(script.get("video", {}).get("status", "")).lower()
        if existing_status == "completed":
            continue
        if wait and existing_status == "submitted" and script.get("video", {}).get("video_id"):
            try:
                completed = client.wait_for_completion(script["video"]["video_id"], timeout_seconds=timeout_seconds)
            except HeyGenError as exc:
                script["video"]["status"] = "error"
                script["video"]["error"] = str(exc)
                script["video"]["updated_at"] = datetime.now().isoformat()
            else:
                detail = completed.detail.get("data", {})
                script["video"]["status"] = completed.status
                script["video"]["video_url"] = detail.get("video_url") or detail.get("url", "")
                script["video"]["thumbnail_url"] = detail.get("thumbnail_url", "")
                script["video"]["detail"] = completed.detail
                script["video"]["updated_at"] = datetime.now().isoformat()
            continue
        if existing_status == "submitted":
            continue

        if dry_run:
            script["video"] = {
                "status": "dry_run",
                "video_id": "",
                "video_url": "",
                "spoken_text_preview": client.compose_spoken_text(script)[:250],
                "updated_at": datetime.now().isoformat(),
            }
            continue

        job = client.create_avatar_video(script)
        script["video"] = {
            "status": job.status,
            "video_id": job.video_id,
            "updated_at": datetime.now().isoformat(),
            "request": client.build_video_payload(script),
        }

        if wait:
            try:
                completed = client.wait_for_completion(job.video_id, timeout_seconds=timeout_seconds)
            except HeyGenError as exc:
                script["video"]["status"] = "error"
                script["video"]["error"] = str(exc)
            else:
                detail = completed.detail.get("data", {})
                script["video"]["status"] = completed.status
                script["video"]["video_url"] = detail.get("video_url") or detail.get("url", "")
                script["video"]["thumbnail_url"] = detail.get("thumbnail_url", "")
                script["video"]["detail"] = completed.detail

    save_manifest(manifest_path, manifest)
    print(f"Updated video state in {manifest_path}")
    return manifest_path


def run_publish(config: dict[str, Any], manifest_path: Path, dry_run: bool) -> Path:
    manifest = load_manifest(manifest_path)
    publisher = N8NPublisher(config)
    publishable_scripts: list[dict[str, Any]] = []

    for script in manifest["scripts"]:
        video_state = script.get("video", {})
        video_status = str(video_state.get("status", "")).lower()
        if dry_run or video_status == "completed" or video_state.get("video_url"):
            publishable_scripts.append(script)
        else:
            script["publish"] = {
                "status": "skipped",
                "reason": "video_not_ready",
                "updated_at": datetime.now().isoformat(),
            }

    batch_results = publisher.publish_batch(publishable_scripts, dry_run=dry_run)

    for script in manifest["scripts"]:
        if script["script_id"] in batch_results:
            script["publish"] = batch_results.get(script["script_id"], {})
            script["publish"]["updated_at"] = datetime.now().isoformat()

    save_manifest(manifest_path, manifest)
    print(f"Updated publish state in {manifest_path}")
    return manifest_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dayou content automation pipeline.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Path to config.yaml")

    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate weekly scripts")
    generate.add_argument("--week-of", help="Any date inside the target week, format YYYY-MM-DD")
    generate.add_argument("--count", type=int, default=7, help="Number of scripts to generate")
    generate.add_argument("--dry-run", action="store_true", help="Use fallback copy instead of LLM calls")

    video = subparsers.add_parser("video", help="Generate HeyGen videos from a manifest")
    video.add_argument("--manifest", help="Path to manifest.json; defaults to latest")
    video.add_argument("--wait", action="store_true", help="Poll HeyGen until completion")
    video.add_argument("--timeout-seconds", type=int, default=900, help="Max wait time when --wait is set")
    video.add_argument("--dry-run", action="store_true", help="Skip live HeyGen calls")

    publish = subparsers.add_parser("publish", help="Send publish jobs to n8n")
    publish.add_argument("--manifest", help="Path to manifest.json; defaults to latest")
    publish.add_argument("--dry-run", action="store_true", help="Print payloads into the manifest without sending")

    full = subparsers.add_parser("full", help="Run generate, video, and publish in sequence")
    full.add_argument("--week-of", help="Any date inside the target week, format YYYY-MM-DD")
    full.add_argument("--count", type=int, default=7, help="Number of scripts to generate")
    full.add_argument("--wait", action="store_true", help="Poll HeyGen until completion")
    full.add_argument("--timeout-seconds", type=int, default=900, help="Max wait time when --wait is set")
    full.add_argument("--dry-run", action="store_true", help="Skip live LLM, HeyGen, and n8n calls")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    config_path = Path(args.config).resolve()
    config = load_config(config_path)

    if args.command == "generate":
        week_of = date.fromisoformat(args.week_of) if args.week_of else None
        run_generate(config_path=config_path, week_of=week_of, count=args.count, dry_run=args.dry_run)
        return

    if args.command == "video":
        manifest_path = resolve_manifest_path(config, getattr(args, "manifest", None))
        run_video(config=config, manifest_path=manifest_path, wait=args.wait, dry_run=args.dry_run, timeout_seconds=args.timeout_seconds)
        return

    if args.command == "publish":
        manifest_path = resolve_manifest_path(config, getattr(args, "manifest", None))
        run_publish(config=config, manifest_path=manifest_path, dry_run=args.dry_run)
        return

    if args.command == "full":
        week_of = date.fromisoformat(args.week_of) if args.week_of else None
        manifest_path = run_generate(config_path=config_path, week_of=week_of, count=args.count, dry_run=args.dry_run)
        run_video(config=config, manifest_path=manifest_path, wait=args.wait, dry_run=args.dry_run, timeout_seconds=args.timeout_seconds)
        run_publish(config=config, manifest_path=manifest_path, dry_run=args.dry_run)
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
