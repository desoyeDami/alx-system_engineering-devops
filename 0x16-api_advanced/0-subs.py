#!/usr/bin/python3
"""Quering Reddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # parse JSON response to extract no of subscribers
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
