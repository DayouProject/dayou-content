from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Mapping
from urllib import request


class N8NPublisher:
    """Dispatches normalized publish jobs to an n8n webhook."""

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.publish_config = dict(config["publish"])
        self.n8n_config = dict(config["n8n"])
        self.webhook_url = f"{self.n8n_config['base_url'].rstrip('/')}{self.n8n_config['webhook_path']}"
        token_env = self.n8n_config.get("auth_token_env", "")
        self.auth_token = os.getenv(token_env, "") if token_env else ""

    def build_payload(self, script: Mapping[str, Any], channel: Mapping[str, Any]) -> dict[str, Any]:
        video_detail = dict(script.get("video", {}))
        return {
            "source": self.n8n_config.get("source_label", "dayou-content"),
            "timestamp": datetime.now().isoformat(),
            "platform": channel["platform"],
            "account_label": channel.get("account_label"),
            "scheduled_for": script.get("scheduled_for"),
            "title": script.get("title"),
            "caption": script.get("caption"),
            "hashtags": script.get("hashtags", []),
            "video_url": video_detail.get("video_url"),
            "video_id": video_detail.get("video_id"),
            "status": video_detail.get("status"),
            "script_id": script.get("script_id"),
            "source_id": script.get("source_id"),
            "source_path": script.get("source_path"),
        }

    def publish_via_n8n(self, payload: Mapping[str, Any], dry_run: bool = False) -> dict[str, Any]:
        if dry_run:
            return {"status": "dry_run", "payload": payload}

        headers = {"Content-Type": "application/json"}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"

        http_request = request.Request(
            self.webhook_url,
            headers=headers,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            method="POST",
        )
        with request.urlopen(http_request, timeout=30) as response:
            raw_body = response.read().decode("utf-8")
            try:
                response_data = json.loads(raw_body)
            except json.JSONDecodeError:
                response_data = {"body": raw_body}
            return {"status": "sent", "code": response.status, "response": response_data}

    def publish_script(self, script: Mapping[str, Any], dry_run: bool = False) -> dict[str, Any]:
        results: dict[str, Any] = {}
        for channel in self.publish_config.get("channels", []):
            if not channel.get("enabled", False):
                continue
            payload = self.build_payload(script, channel)
            results[channel["platform"]] = self.publish_via_n8n(payload, dry_run=dry_run)
        return results

    def publish_batch(self, scripts: list[Mapping[str, Any]], dry_run: bool = False) -> dict[str, Any]:
        return {str(script["script_id"]): self.publish_script(script, dry_run=dry_run) for script in scripts}
