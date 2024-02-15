#!/usr/bin/python3
"""
important script
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Get the number of subscribers for a given subreddit.
    """
    b_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    x = False
    if subreddit:
        if after is None:
            url = b_url
        else:
            url = b_url + after
        res = requests.get(url, headers={'User-Agent': 'A Python script'},
                           allow_redirects=False)
        if res.status_code == 200:
            json_res = res.json()
            childern = json_res.get('data').get('children')
            if json_res.get('data').get('after') is None:
                if len(childern) == 0:
                    return hot_list
                x = True
            for i in range(len(childern)):
                hot_list.append(childern[i].get('data').get('title'))
            after_post = f"&after={json_res.get('data').get('after')}"
            if x:
                return hot_list
        else:
            return None
        return recurse(subreddit, hot_list, after=after_post)
