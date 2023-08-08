#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers for the subreddit.
             Returns 0 if the subreddit is invalid or an error occurs.
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "CustomBot"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        data = res.json()
        if not data:
            return 0
        if "data" not in data:
            return 0
        return data["data"]["subscribers"]
    except requests.RequestException as e:
        return 0
