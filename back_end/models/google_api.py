"""
This module contains functions that retrieves data
from the google books and search APIs
"""


import requests
from models.handle_api_keys import google_key

title = 'Data Structure'

def get_books(q=None):
    """ Get books from the books API based on query string """

    if q is None or q == '':
        return None

    base = "https://www.googleapis.com/books/v1/volumes"
    url = f"{base}?q={q}&key={google_key}"

    books = requests.get(url)

    return books.json()['items']

def get_sites(q=None):
    """ Get articles from sites based on query """

    if q is None or q == '':
        return None

    base = "https://www.googleapis.com/customsearch/v1"
    url = f"{base}?q={q}&key={google_key}&cx=15b00fc86bf1d4b2c"

    sites = requests.get(url)

    return sites.json()['items']

def get_videos(q=None):
    """ Get videos from youtube base on query """

    if q is None or q == '':
        return None

    base = "https://www.googleapis.com/youtube/v3/search"
    url = f"{base}?part=snippet&q={q}&type=video&key={google_key}"

    videos = requests.get(url)

    return videos.json()['items']
