#!/usr/bin/python3
""" Querying Reddit"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the top 10 hot
    posts for a given subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'mybot/0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    else:
        print(None)