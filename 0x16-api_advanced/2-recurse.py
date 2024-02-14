#!/usr/bin/python3
"""
important script
"""
import requests
def recurse(subreddit, hot_list=[], after=None):
    """
    Get the number of subscribers for a given subreddit.
    """
    if subreddit:
        if after is None:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
        else:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100' + after
        res = requests.get(url, headers={'User-Agent': 'A Python script'}, allow_redirects=False)
        if res.status_code == 200:
            json_res = res.json()
            if json_res.get('data').get('after') is None:
                if len(json_res.get('data').get('children')) == 0:
                    return hot_list
                x = True
            for i in range(len(json_res.get('data').get('children'))):
                hot_list.append(json_res.get('data').get('children')[i].get('data').get('title'))
            after_post = f"&after={json_res.get('data').get('after')}"
            if x:
                return hot_list
        else:
            return None
        return recurse(subreddit, hot_list, after=after_post)
