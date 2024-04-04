#!/usr/bin/env python3
""" BaseCaching module """

caching = __import__('base_caching')


class LIFOCache(caching.BaseCaching):
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
