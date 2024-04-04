#!/usr/bin/env python3
""" BaseCaching module """


class BaseCaching():
    """
        BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError(
                "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError(
                "get must be implemented in your cache class")


class LIFOCache(BaseCaching):
    """ last in first out caching system """
    # save the last accessed key for faster and easier removal
    __last_key = None

    def __init__(self):
        """ initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.cache_data.pop(self.__last_key)
                    print("DISCARD: {}".format(self.__last_key))

            self.cache_data[key] = item
            self.__last_key = key

    def get(self, key):
        """ Get an item by key """
        if not key:
            return None
        return self.cache_data[key]
