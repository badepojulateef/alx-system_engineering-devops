#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after="", word_obj={}):
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
    if not word_obj:
        for word in word_list:
            word_obj[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_obj.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))

        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower, w[1]))

        return None

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
                title = article["data"]["title"]
                lower = [s.lower() for s in title.split(" ")]

                for w in word_list:
                    word_obj[w] += lower.count(w.lower())

    except requests.RequestException as e:
        return None
    count_words(subreddit, word_list, after, word_obj)
