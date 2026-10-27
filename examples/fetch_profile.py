#!/usr/bin/env python3
"""Fetch a public Instagram profile via a low volume Instagram scraper (Socify).

Usage:
  export SOCIFY_API_KEY=...
  python examples/fetch_profile.py natgeo

Signup: https://trysocify.com/register
Guide:  https://trysocify.com/use-cases/best-low-volume-instagram-scrapers-2026
"""

from __future__ import annotations

import json
import sys

from low_volume_instagram_scraper import InstagramClient


def main() -> None:
    username = sys.argv[1] if len(sys.argv) > 1 else "instagram"
    with InstagramClient() as client:
        data = client.profile(username)
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
