#!/usr/bin/python3
"""Quering Reddit"""

import requests


def top_ten(subreddit):
    """query a subreddit and retrive no of top 10 hot posts"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
