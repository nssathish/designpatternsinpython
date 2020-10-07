"""
    Singleton Pattern
    -----------------
    The singleton pattern restricts the instantiation of a class
    to only one object.
    To ensure that this works, we need to make sure about the
    following
    1. Prevent the instantiation of the close more than once
    2. Prevent cloning (Prototype should be an anti-pattern here)

    Use Cases
    ---------
    1. Scenario when there is only one object is enough
    2. Scenario when there is an object capable of maintaining
    a global state for your program
"""
import urllib.parse
import urllib.request


class SingletonType(type):
    # '_' - underscore says that the field/property is private
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            if res.code == 200:
                the_page = res.read()
                print(the_page)
                urls = self.urls
                urls.append(url)
                self.urls = urls


if __name__ == "__main__":
    f1 = URLFetcher()
    f2 = URLFetcher()

    print(f'{id(f1)} is {id(f2)}? {f1 is f2}')
