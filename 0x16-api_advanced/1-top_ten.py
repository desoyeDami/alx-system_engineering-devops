#!/usr/bin/python3
"""Quering Reddit"""

import requests


def top_ten(subreddit):
    """query a subreddit and retrive no of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'My user Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # parse JSON response to extract no of subscribers
        data = response.json()
        posts = data['data']['children']
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print(None)
