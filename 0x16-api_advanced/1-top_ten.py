#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Retrieve the top ten posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        str: Title of the top ten posts for the subreddit.
             Returns None if the subreddit is invalid or an error occurs.
    """
    if not subreddit:
        print("None")

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "CustomBot"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}

    try:
        res = requests.get(
                url,
                params=params,
                headers=headers,
                allow_redirects=False
            )
        if res.status_code != 200:
            print("None")
            return
        data = res.json()
        posts = []
        if "data" in data:
            posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except requests.RequestException as e:
        print("None")
