#!/usr/bin/env python3
""" simple pagination """


import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """Return a tuple of size two containing a
        start index and an end index."""
        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page of the dataset"""
        # type checking and error handling
        assert (type(page) is int and type(page_size) is int)
        assert (page > 0 and page_size > 0)
        page_range = self.index_range(page, page_size)
        self.dataset()
        return self.__dataset[page_range[0]:page_range[1]]
