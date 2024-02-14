import requests
def recurse(subreddit, hot_list=[], after=None):
    """
    Get the number of subscribers for a given subreddit.
    """
    if subreddit:
        if after is None:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=1'
        else:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=1' + after
        res = requests.get(url, headers={'User-Agent': 'A Python script'}, allow_redirects=False)
        if res.status_code == 200:
            json_res = res.json()
            hot_list.append(json_res['data']['children'][0]['data']['title'])
            after_post = f'&after={json_res["data"]["after"]}'
        else:
            return None
        if json_res['data']['after'] is None:
            return hot_list
        return recurse(subreddit, hot_list, after=after_post)
