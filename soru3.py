import requests
from typing import Callable, Generator


def error_handler(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> dict:
        results = None
        response = func(*args, **kwargs)
        if response.ok:
            response = response.json()
            results = response.get('results')
        return results

    return wrapper


def converter(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> dict:
        response = func(*args, **kwargs)
        return list(response)

    return wrapper


class RequestData:
    """
        RequestData
    """
    BASE_URL = 'https://randomuser.me/api/'

    def __init__(self, count: str, *args, **kwargs):
        self.url = self.BASE_URL + '?results={}'.format(count)

    @error_handler
    def _make_request(self):
        response = requests.get(self.url)
        return response

    @converter
    def get_location(self):
        results = self._make_request()
        for item in results:
            yield item.get('location')

    @converter
    def get_login(self):
        results = self._make_request()
        for item in results:
            yield item.get('login')

def print_streets(amount):

    results = RequestData(amount)
    location = results.get_location()

    for i in range(amount):
        print(location[i]['street'])

def print_names(amount):

    results = RequestData(amount)
    names = results.get_login()

    for i in range(amount):
        print(names[i]['username'])

print_streets(20)
print_names(100)