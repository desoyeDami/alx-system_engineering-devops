#!/usr/bin/python3
""" Querying Reddit """
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively query a subreddit and return a list of titles of all hot posts."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'mybot/0.1'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after", None)

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
