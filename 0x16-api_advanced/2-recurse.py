import requests
def recurse(subreddit, hot_list=[], after=None):
    """
    Get the number of subscribers for a given subreddit.
    """
    if subreddit:
        if after == None:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=1'
        else:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=1' + after
        res = requests.get(url,headers={'User-Agent': 'A Python script'}, allow_redirects=False)
        if res.status_code == 200:
            json_res = res.json()
            hot_list.append(json_res.get('data').get('children').get('data').get('title'))
            after_post = f'&after={json_res.get('data').get('after')}'
        else:
            return None
        if json_res.get('data').get('after') == None:
            return hot_list
        recurse(subreddit, hot_list=[], after=after_post)
