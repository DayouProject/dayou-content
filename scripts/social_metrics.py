#!/usr/bin/env python3
"""Collect daily social metrics and append them to workspace/metrics/*.jsonl."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def load_config(path: Path) -> dict[str, Any]:
    """Load the repo config file, which is JSON content stored in config.yaml."""
    return json.loads(path.read_text(encoding="utf-8"))


def request_json(url: str, headers: dict[str, str] | None = None) -> dict[str, Any]:
    """Fetch a JSON payload with stdlib urllib only."""
    req = Request(url, headers=headers or {})
    with urlopen(req, timeout=30) as response:
        return json.load(response)


def save_metrics(output_root: Path, records: list[dict[str, Any]]) -> Path:
    """Append one JSON object per line to the current day metrics file."""
    metrics_dir = output_root / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)
    day = datetime.utcnow().date().isoformat()
    target = metrics_dir / f"{day}.jsonl"
    with target.open("a", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return target


class XCollector:
    """Collect follower and recent tweet metrics from the X API v2."""

    platform = "x"

    def __init__(self, handle: str, bearer_token: str) -> None:
        self.handle = handle.removeprefix("@")
        self.bearer_token = bearer_token
        self.base_url = "https://api.twitter.com/2"

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.bearer_token}"}

    def _user(self) -> dict[str, Any]:
        params = urlencode({"user.fields": "public_metrics,username,name"})
        url = f"{self.base_url}/users/by/username/{self.handle}?{params}"
        return request_json(url, self.headers)["data"]

    def get_followers(self) -> dict[str, Any]:
        user = self._user()
        metrics = user.get("public_metrics", {})
        return {
            "handle": f"@{user['username']}",
            "display_name": user.get("name"),
            "followers": metrics.get("followers_count", 0),
            "following": metrics.get("following_count", 0),
            "tweet_count": metrics.get("tweet_count", 0),
            "listed_count": metrics.get("listed_count", 0),
            "user_id": user["id"],
        }

    def get_recent_posts_metrics(self, limit: int = 5) -> list[dict[str, Any]]:
        user_id = self._user()["id"]
        params = urlencode(
            {
                "max_results": str(limit),
                "exclude": "replies,retweets",
                "tweet.fields": "created_at,public_metrics,text",
            }
        )
        url = f"{self.base_url}/users/{user_id}/tweets?{params}"
        tweets = request_json(url, self.headers).get("data", [])
        return [
            {
                "id": tweet["id"],
                "created_at": tweet.get("created_at"),
                "text": tweet.get("text", "")[:120],
                **tweet.get("public_metrics", {}),
            }
            for tweet in tweets
        ]


class YouTubeCollector:
    """Collect subscriber and recent video metrics from YouTube Data API v3."""

    platform = "youtube"

    def __init__(self, handle: str, api_key: str) -> None:
        self.handle = handle
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def _api_get(self, endpoint: str, **params: str) -> dict[str, Any]:
        params["key"] = self.api_key
        url = f"{self.base_url}/{endpoint}?{urlencode(params)}"
        return request_json(url)

    def _channel(self) -> dict[str, Any]:
        cleaned = self.handle.removeprefix("@")
        payload = self._api_get(
            "channels",
            part="snippet,statistics",
            forHandle=cleaned,
        )
        items = payload.get("items", [])
        if not items:
            raise ValueError(f"No YouTube channel found for handle: {self.handle}")
        return items[0]

    def get_followers(self) -> dict[str, Any]:
        channel = self._channel()
        stats = channel.get("statistics", {})
        snippet = channel.get("snippet", {})
        return {
            "handle": self.handle,
            "channel_id": channel["id"],
            "title": snippet.get("title"),
            "subscribers": int(stats.get("subscriberCount", 0)),
            "video_count": int(stats.get("videoCount", 0)),
            "view_count": int(stats.get("viewCount", 0)),
        }

    def get_recent_posts_metrics(self, limit: int = 5) -> list[dict[str, Any]]:
        channel_id = self._channel()["id"]
        search_payload = self._api_get(
            "search",
            part="id",
            channelId=channel_id,
            maxResults=str(limit),
            order="date",
            type="video",
        )
        video_ids = [
            item["id"]["videoId"]
            for item in search_payload.get("items", [])
            if item.get("id", {}).get("videoId")
        ]
        if not video_ids:
            return []
        videos_payload = self._api_get(
            "videos",
            part="snippet,statistics",
            id=",".join(video_ids),
        )
        videos = videos_payload.get("items", [])
        return [
            {
                "id": video["id"],
                "published_at": video.get("snippet", {}).get("publishedAt"),
                "title": video.get("snippet", {}).get("title"),
                "views": int(video.get("statistics", {}).get("viewCount", 0)),
                "likes": int(video.get("statistics", {}).get("likeCount", 0)),
                "comments": int(video.get("statistics", {}).get("commentCount", 0)),
            }
            for video in videos
        ]


class StubCollector:
    """Placeholder collector for platforms whose APIs are not ready yet."""

    def __init__(self, platform: str, account: str) -> None:
        self.platform = platform
        self.account = account

    def get_followers(self) -> dict[str, Any]:
        # TODO: TikTok integration should move from this stub to approved TikTok
        # endpoints. Start with /v2/user/info/ for profile data and pair it with
        # /v2/video/list/ or /v2/video/query/ for recent posts once app review
        # and the required scopes are approved for the Dayou account.
        # TODO: Instagram Graph API should use /{ig-user-id}?fields=followers_count
        # once the account is switched to Business and linked to a Facebook Page.
        return {
            "handle": self.account,
            "status": "stub",
            "todo": self._todo_message(),
        }

    def get_recent_posts_metrics(self, limit: int = 5) -> list[dict[str, Any]]:
        # TODO: TikTok should use /v2/video/list/ for recent uploads and
        # /v2/video/query/ for refreshed per-video metadata after approval.
        # TODO: Instagram should use /{ig-user-id}/media and
        # /{ig-media-id}/insights for per-post metrics.
        _ = limit
        return []

    def _todo_message(self) -> str:
        if self.platform == "tiktok":
            return "TODO: integrate TikTok Business API after app approval."
        return "TODO: integrate Instagram Graph API after Business account setup."


def requested_platforms(platform: str) -> list[str]:
    """Expand the CLI platform selector into concrete platform names."""
    return ["x", "tiktok", "youtube", "instagram"] if platform == "all" else [platform]


def default_accounts(account: str | None) -> dict[str, str]:
    """Return default account identifiers for each supported platform."""
    return {
        "x": account or os.getenv("TWITTER_HANDLE") or os.getenv("X_HANDLE") or "TBD",
        "tiktok": account or "@dayou.wisdom",
        "youtube": account or os.getenv("YOUTUBE_CHANNEL_HANDLE") or "@dayou.wisdom",
        "instagram": account or "@dayou.wisdom",
    }


def build_collector(platform: str, account: str) -> Any:
    """Construct one collector for a single platform."""
    if platform == "x":
        token = os.getenv("TWITTER_BEARER_TOKEN")
        if not token:
            raise ValueError("TWITTER_BEARER_TOKEN is required for X metrics.")
        return XCollector(account, token)
    if platform == "youtube":
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY is required for YouTube metrics.")
        return YouTubeCollector(account, api_key)
    return StubCollector(platform, account)


def collect_metrics(collector: Any) -> dict[str, Any]:
    """Collect a normalized metrics payload for a single platform."""
    collected_at = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return {
        "date": datetime.utcnow().date().isoformat(),
        "collected_at": collected_at,
        "platform": collector.platform,
        "followers": collector.get_followers(),
        "recent_posts_metrics": collector.get_recent_posts_metrics(),
    }


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        choices=["x", "tiktok", "youtube", "instagram", "all"],
        default="all",
        help="Platform to collect metrics for.",
    )
    parser.add_argument(
        "--account",
        help="Override the default account handle or channel handle for the platform.",
    )
    return parser.parse_args()


def main() -> int:
    """CLI entry point."""
    args = parse_args()
    config = load_config(Path("config.yaml"))
    output_root = Path(config["project"]["output_root"])
    records: list[dict[str, Any]] = []
    failures = 0
    accounts = default_accounts(args.account)
    for platform in requested_platforms(args.platform):
        try:
            collector = build_collector(platform, accounts[platform])
            records.append(collect_metrics(collector))
        except Exception as exc:  # noqa: BLE001
            failures += 1
            records.append(
                {
                    "date": datetime.utcnow().date().isoformat(),
                    "collected_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
                    "platform": platform,
                    "status": "error",
                    "error": str(exc),
                }
            )
    path = save_metrics(output_root, records)
    print(json.dumps({"saved_to": str(path), "records": records}, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
