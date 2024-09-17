"""
The module contain function that retrieves data from
the Udemy API
"""


import requests
from models.handle_api_keys import udemy_key


def get_courses(q=None):
    """ Get courses from udemy base on search query """

    if q is None or q == '':
        return None

    header = {"Authorization": f"{udemy_key}"}
    base = "https://www.udemy.com/api-2.0/courses/"
    url = f"{base}?search={q}"

    courses = requests.get(url, headers=header)

    return courses.json()['results']
