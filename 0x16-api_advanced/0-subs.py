#!/usr/bin/python3
""" Subreddit Subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 1
