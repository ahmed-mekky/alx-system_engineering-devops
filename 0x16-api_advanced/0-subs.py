#!/usr/bin/python3
"""
important script
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    """
    subs = 0
    if subreddit:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        res = requests.get(url, headers={'User-Agent': 'A Python script'},
                           allow_redirects=False)
        if res.status_code == 200:
            subs = res.json().get('data').get('subscribers')
    return subs
