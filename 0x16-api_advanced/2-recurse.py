#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Retrieve the top ten posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        str: Title of the top ten posts for the subreddit.
             Returns None if the subreddit is invalid or an error occurs.
    """
    if subreddit is None:
        return None
    if after is None:
        return hot_list

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "CustomBot"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}

    try:
        res = requests.get(
                url,
                params=params,
                headers=headers,
                allow_redirects=False
            )

        # print('code', res.status_code)
        # print(res.json())
        if res.status_code != 200:
            return None

        after_res = res.json().get("data").get("after")
        # print('after_res', after_res)
        # if after_res is not None:
        # after = after_res
        # recurse(subreddit, hot_list, after)

        if after_res is None:
            articles = res.json().get("data").get("children")
            # print('r => ', r[0]["data"]["title"])
            for article in articles:
                hot_list.append(article["data"]["title"])
            # print('hot_list => ', hot_list)
            return hot_list

    except requests.RequestException as e:
        return None

    after = after_res
    return recurse(subreddit, hot_list, after)
