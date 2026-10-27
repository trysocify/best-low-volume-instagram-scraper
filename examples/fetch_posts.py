#!/usr/bin/env python3
"""List recent public Instagram posts — low volume Instagram scraper example.

Signup: https://trysocify.com/register
Use case: https://trysocify.com/use-cases/best-low-volume-instagram-scrapers-2026
"""

from __future__ import annotations

import json
import sys

from low_volume_instagram_scraper import InstagramClient


def main() -> None:
    username = sys.argv[1] if len(sys.argv) > 1 else "natgeo"
    with InstagramClient() as client:
        data = client.posts(username=username)
    print(json.dumps(data, indent=2, default=str))


if __name__ == "__main__":
    main()
