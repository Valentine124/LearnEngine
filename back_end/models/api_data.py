""" This module get the data from the api and store
it on the database"""


from models import storage
from models.google_api import get_books, get_videos, get_sites
from models.udemy_api import get_courses
from models.resources import Resources


def resource_data(title=None):
    """ Get the resources from the api and save it
    it to the database """

    if title is None or title == '':
        return None

    save_books(title)
    save_sites(title)
    save_videos(title)
    save_courses(title)

def save_books(title):
    """ Save books from API to database """

    books = get_books(title)

    for item in books:
        resource = Resources()
        resource.title = item['volumeInfo']['title']
        resource.description = trunc_str(item['volumeInfo']['description'])
        resource.origin = 'Google Books'
        resource.type = 'book'
        resource.url = item['selfLink']
        resource.img = item['volumeInfo']['imageLinks']['thumbnail']

        storage.new(resource)

def save_sites(title):
    """ Save search result to database """

    sites = get_sites(title)

    for item in sites:
        resource = Resources()
        resource.title = item['title']
        resource.description = trunc_str(item['snippet'])
        resource.origin = 'Google Search'
        resource.type = 'articles'
        resource.url = item['link']
        resource.img = 'https://img.freepik.com/premium-photo/online-article-concept-illustration_1254992-270732.jpg'

        storage.new(resource)

def save_videos(title):
    videos = get_videos(title)

    for item in videos:
        resource = Resources()
        resource.title = item['snippet']['title']
        resource.description = trunc_str(item['snippet']['description'])
        resource.origin = 'Youtube'
        resource.type = 'video'
        resource.url = f'https://www.youtube.com/watch?v={item["id"]["videoId"]}'
        resource.img = item['snippet']['thumbnails']['default']['url']

        storage.new(resource)

def save_courses(title):
    courses = get_courses(title)

    for item in courses:
        resource = Resources()
        resource.title = item['title']
        resource.description = trunc_str(item['headline'])
        resource.origin = 'Udemy'
        resource.type = 'course'
        resource.url = item['url']
        resource.img = item['image_125_H']

        storage.new(resource)

def trunc_str(str):
    """ Truncate long string """

    last = 60

    try:
        last = str.index('.')
    except:
        return str

    return str[0:last]
