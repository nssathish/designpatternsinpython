"""
Bridge Pattern
--------------
A structural pattern unlike the adapter pattern, is to
1. Design up-front to decouple an implementation from its abstraction

Use cases
---------
1. Used when we want to share an implementation among multiple objects
    1. By defining an abstraction that applies to all classes
    2. By defining a separate interface for the different objects involved
"""
from urllib import request
from abc import ABC, ABCMeta, abstractmethod


class ResourceContent(ABC):
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the implementor.
    """

    def __init__(self, implementation) -> None:
        self._implementation = implementation

    def show_content(self, path):
        print(self._implementation.fetch(path))


class ResourceContentFetcher(metaclass=ABCMeta):

    @abstractmethod
    def fetch(self, path):
        pass


class URLFetcher(ResourceContentFetcher):

    def fetch(self, path):
        req = request.Request(path)
        with request.urlopen(req) as res:
            if res.code == 200:
                the_page = res.read()
                return the_page


class LocalFileFetcher(ResourceContentFetcher):

    def fetch(self, path):
        with open(path) as f:
            return f.read()


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content("http://google.com")

    print("=====================")
    local_file_fetcher = LocalFileFetcher()
    iface = ResourceContent(local_file_fetcher)
    iface.show_content("file.txt")


if __name__ == "__main__":
    main()
