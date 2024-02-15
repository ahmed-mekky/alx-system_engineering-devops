#!/usr/bin/python3
"""
important script
"""
import requests


def top_ten(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    """
    if subreddit:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=9'
        # should be 10 but the api have an error
        res = requests.get(url, headers={'User-Agent': 'A Python script'},
                           allow_redirects=False)
        if res.status_code == 200:
            for child in res.json().get('data').get('children'):
                print(child.get('data').get('title'))
        else:
            print('None')
