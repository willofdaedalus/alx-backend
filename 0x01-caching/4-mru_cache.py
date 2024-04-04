#!/usr/bin/env python3
""" BaseCaching module """

from datetime import datetime
caching = __import__("base_caching")


class MRUCache(caching.BaseCaching):
    """ last in first out caching system """
    # save the last accessed key for faster and easier removal
    __item_tracker = {}

    def __init__(self):
        """ initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    to_rm = max(self.__item_tracker)
                    self.cache_data.pop(to_rm)
                    self.__item_tracker.pop(to_rm)
                    print("DISCARD: {}".format(to_rm))

            self.cache_data[key] = item
            self.__item_tracker[key] = datetime.now()

    def get(self, key):
        """ Get an item by key """
        if key not in self.cache_data:
            return None
        self.__item_tracker[key] = datetime.now()
        return self.cache_data[key]
