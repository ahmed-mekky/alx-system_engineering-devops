#!/usr/bin/python3
"just for the module to be documented"
import requests


def count_words(subreddit, word_list, after=None, count=None):
    """
    Count occurrences of words in the titles of posts from a given subreddit.
    """
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    x = False
    after_post = after
    if count is None:
        counter = {}
    else:
        counter = count

    if after is None:
        url = base_url
    else:
        url = base_url + after

    res = requests.get(url, headers={'User-Agent': 'A Python script'},
                       allow_redirects=False)

    if res.status_code == 200:
        json_res = res.json()
        children = json_res.get('data', {}).get('children', [])

        if json_res.get('data', {}).get('after') is None:
            if len(children) == 0:
                return counter
            x = True

        # Extract words from titles and update the counter
        for post in children:
            title = post.get('data', {}).get('title', '')
            words = title.split()
            for word in words:
                clean_word = ''.join(c for c in word if c.isalpha()).lower()
                if clean_word in word_list:
                    counter[clean_word] = counter.get(clean_word, 0) + 1

        after_post = f"&after={json_res.get('data', {}).get('after')}"
        if x:
            for key, val in sorted(counter.items()):
                print(f"{key}: {val}")
            exit()

    return count_words(subreddit, word_list, after=after_post, count=counter)
