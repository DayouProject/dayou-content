from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any, Mapping
from urllib import parse, request


class HeyGenError(RuntimeError):
    """Raised when HeyGen rejects a request or returns an unexpected payload."""


@dataclass(slots=True)
class HeyGenVideoJob:
    video_id: str
    status: str
    detail: dict[str, Any]


class HeyGenClient:
    """Minimal HeyGen API client for avatar video creation."""

    def __init__(self, config: Mapping[str, Any]) -> None:
        self.base_url = str(config["base_url"]).rstrip("/")
        self.api_key = os.getenv(str(config["api_key_env"]), "")
        self.timeout_seconds = int(config.get("timeout_seconds", 60))
        self.polling_interval_seconds = int(config.get("polling_interval_seconds", 20))
        self.video_config = dict(config.get("video", {}))
        self.avatar_config = dict(config.get("avatar", {}))

    @property
    def is_configured(self) -> bool:
        return bool(self.api_key)

    def _headers(self) -> dict[str, str]:
        if not self.api_key:
            raise HeyGenError("Missing HEYGEN_API_KEY environment variable.")
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }

    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        payload = kwargs.get("json")
        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")

        http_request = request.Request(
            url=f"{self.base_url}{path}",
            data=data,
            headers=self._headers(),
            method=method,
        )
        try:
            with request.urlopen(http_request, timeout=self.timeout_seconds) as response:
                data = json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            raise HeyGenError(str(exc)) from exc

        if isinstance(data, dict) and data.get("error"):
            raise HeyGenError(str(data["error"]))
        return data

    def list_avatars(self) -> dict[str, Any]:
        return self._request("GET", "/v2/avatars")

    def list_voices(self) -> dict[str, Any]:
        return self._request("GET", "/v2/voices")

    def compose_spoken_text(self, script: Mapping[str, Any]) -> str:
        body_points = script.get("body_points", [])
        segments = [str(script.get("hook", "")).strip()]
        segments.extend(str(point).strip() for point in body_points if str(point).strip())
        segments.append(str(script.get("cta", "")).strip())
        return " ".join(segment for segment in segments if segment)

    def build_video_payload(self, script: Mapping[str, Any]) -> dict[str, Any]:
        spoken_text = self.compose_spoken_text(script)
        return {
            "video_inputs": [
                {
                    "character": {
                        "type": "avatar",
                        "avatar_id": self.avatar_config["avatar_id"],
                        "avatar_style": self.avatar_config.get("avatar_style", "normal"),
                    },
                    "voice": {
                        "type": "text",
                        "input_text": spoken_text,
                        "voice_id": self.avatar_config["voice_id"],
                        "speed": float(self.avatar_config.get("rate", 1.0)),
                        "pitch": float(self.avatar_config.get("pitch", 0.0)),
                    },
                }
            ],
            "dimension": {
                "width": int(self.video_config.get("width", 1080)),
                "height": int(self.video_config.get("height", 1920)),
            },
        }

    def create_avatar_video(self, script: Mapping[str, Any]) -> HeyGenVideoJob:
        data = self._request("POST", "/v2/video/generate", json=self.build_video_payload(script))
        video_id = data.get("data", {}).get("video_id")
        if not video_id:
            raise HeyGenError(f"Missing video_id in response: {data}")
        return HeyGenVideoJob(video_id=video_id, status="submitted", detail=data)

    def get_video_status(self, video_id: str) -> HeyGenVideoJob:
        encoded_video_id = parse.quote(video_id, safe="")
        data = self._request("GET", f"/v1/video_status.get?video_id={encoded_video_id}")
        status = str(data.get("data", {}).get("status") or data.get("status") or "unknown")
        return HeyGenVideoJob(video_id=video_id, status=status, detail=data)

    def wait_for_completion(self, video_id: str, timeout_seconds: int = 900) -> HeyGenVideoJob:
        deadline = time.monotonic() + timeout_seconds
        last_status = "submitted"

        while time.monotonic() < deadline:
            job = self.get_video_status(video_id)
            last_status = job.status
            if job.status.lower() in {"completed", "failed"}:
                return job
            time.sleep(self.polling_interval_seconds)

        raise HeyGenError(f"Timed out waiting for video {video_id}; last status was {last_status}.")
