#!/usr/bin/env python3
""" BaseCaching module """

caching = __import__('base_caching')


class FIFOCache(caching.BaseCaching):
    """ first in first out caching system """

    def __init__(self):
        """ initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                to_rm = next(iter(self.cache_data))
                print("DISCARD: {}".format(to_rm))
                self.cache_data.pop(to_rm)

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not key:
            return None
        return self.cache_data[key]
