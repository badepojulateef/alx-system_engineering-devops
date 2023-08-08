#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
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
        return

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "CustomBot"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"after": after}

    try:
        res = requests.get(
                url,
                params=params,
                headers=headers,
                allow_redirects=False
            )
        
        # print(res.status_code)
        # print(res.json())
        if res.status_code != 200:
            print("None")
            return
        data = res.json()
        articles = data["data"]["children"]

        if not articles:
            return hot_list
        
        for article in articles:
            title = article["data"]["title"]
            hot_list.append(title)

        # Recursive call with the 'after' parameter to get the next page
        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after)

    except requests.RequestException as e:
        print("None")
