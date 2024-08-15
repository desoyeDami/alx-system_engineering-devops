#!/usr/bin/python3
""" Query """
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursively queries hot posts titles in a subreddit and counts
    occurrences of keywords."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'mybot/0.1'}
    params = {'after': after} if after else {}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not word_count:
        for word in word_list:
            word_count[word.lower()] = 0

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        for word in word_count.keys():
            word_count[word] += title.split().count(word)

    after = data.get("after", None)

    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        if word_count:
            sorted_word_count = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
