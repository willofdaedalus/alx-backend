#!/usr/bin/env python3
""" BaseCaching module """

caching = __import__('base_caching')


class BasicCache(caching.BaseCaching):
    """ basic queue based caching system """

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not key:
            return None

        return self.cache_data.get(key)
