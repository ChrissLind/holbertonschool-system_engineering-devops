#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    # Set the Default URL strings
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Python/requests'}
    payload = {'after': after, 'limit': '100'}

    # Get the Response of the Reddit API
    res = requests.get(api_url, headers=user_agent,
                       params=payload, allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code == 200:
        res = res.json()
        hot_posts = res.get('data').get('children')
        after = res.get('data').get('after')

        # Print each hot post title
        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        # Get the next page of hot posts
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
