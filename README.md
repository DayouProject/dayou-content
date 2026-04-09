# Dayou Content Pipeline

Simple Python pipeline for turning Chinese metaphysics source material into short-form avatar videos for overseas TikTok and Instagram audiences.

## What It Does

1. Reads source material from `corpus/`
2. Generates a weekly batch of 7 short scripts with an LLM
3. Sends those scripts to HeyGen for avatar video generation
4. Pushes normalized publish payloads to n8n for final scheduling and posting

The design is intentionally small: one YAML config, a generator, a HeyGen client, an n8n publisher, and a single CLI entrypoint.

## Project Layout

- `config.yaml`: pipeline settings
- `corpus/`: source material for script generation
- `scripts/templates/avatar_script.md`: output format contract for generated scripts
- `scripts/generator.py`: weekly script generation
- `video/heygen_client.py`: HeyGen API client
- `publish/scheduler.py`: n8n publishing client
- `pipeline.py`: CLI entrypoint
- `CULTURAL_TRANSLATION.md`: translation and framing rules for overseas audiences

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set API keys:

```bash
export OPENAI_API_KEY="..."
export HEYGEN_API_KEY="..."
export N8N_WEBHOOK_TOKEN="..."
```

## Config

All runtime behavior is driven from [config.yaml](/Users/lexa/Desktop/lexa/dayou/dayou-content/config.yaml).

Key sections:

- `corpus`: source directories and selection weights
- `llm`: OpenAI-compatible chat-completions settings
- `heygen`: avatar video generation settings
- `publish`: platform schedule and enabled channels
- `persona`: brand voice for the avatar
- `n8n`: webhook transport for publishing

## Usage

Generate a weekly script batch:

```bash
python3 pipeline.py generate --week-of 2026-04-13
```

Dry-run the full flow:

```bash
python3 pipeline.py full --week-of 2026-04-13 --dry-run
```

Generate videos for the latest manifest:

```bash
python3 pipeline.py video --wait
```

Send the latest completed batch to n8n:

```bash
python3 pipeline.py publish
```

## Output

The pipeline writes runtime artifacts to `workspace/`:

- `workspace/scripts/<year-week>/manifest.json`
- `workspace/scripts/<year-week>/scripts/*.md`
- `workspace/videos/`
- `workspace/publish/`

`manifest.json` is the source of truth between stages. The `video` and `publish` steps update it in place.

## Notes

- The `yijing` and `daodejing` corpus files were copied from the omega reference repo as requested.
- The reference repo only exposed one file for each of those sources, so this pipeline treats them as reusable seed texts and expands variety through weekly angles plus the `wisdom/` quote set.
- The LLM client uses a simple OpenAI-compatible REST call instead of a heavyweight SDK so the setup stays easy for a solo founder.
