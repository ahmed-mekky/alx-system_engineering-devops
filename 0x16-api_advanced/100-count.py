#!/usr/bin/python3
"""
important script
"""
import requests
import re


def count_words(subreddit, word_list, after=None):
    """
    Get the number of subscribers for a given subreddit.
    """
    b_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    x = False
    word_counter = {}
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
                    return word_counter
                x = True
            for i in range(len(childern)):
                for word in childern[i].get('data').get('title').split():
                    for l_word in word_list:
                        if word.lower() == re.sub(r"[^\w]", "", l_word).lower():
                            word_counter[word.lower()] = word_counter.get(word, 0) + 1
            after_post = f"&after={json_res.get('data').get('after')}"
            if x:
                for key, val in word_counter.items():
                    print(f"{key}: {val}")
                exit()
        else:
            return None
        return count_words(subreddit, word_list, after=after_post)
