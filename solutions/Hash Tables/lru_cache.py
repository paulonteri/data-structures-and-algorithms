""" 
LRU Cache:

Create a cache for looking up prices of books identified by their ISBN.
You implement lookup, insert, and remove methods. 
Use the Least Recently Used (LRU) policy for cache eviction. 
If an ISBN is already present, insert should not change the price, 
    but it should update that entry to be the most recently used entry. 
    Lookup should also update that entry to be the most recently used entry.
Hint: Amortize the cost of deletion. Alternatively, use an auxiliary data structure.

EPI 12.3
"""

from collections import OrderedDict


class LruCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = OrderedDict()

    def lookup(self, isbn: int):
        if isbn in self.store:
            self.update_to_top(isbn)
            return self.store[isbn]

        return -1

    def insert(self, isbn: int, price: int):
        if isbn in self.store:
            self.update_to_top(isbn)
        else:
            self.store[isbn] = price

        self.check_if_full_and_remove_excess()

    def erase(self, isbn: int):
        if isbn in self.store:
            self.store.pop(isbn)
            return True

        return False

    def update_to_top(self, isbn: int):
        price = self.store.pop(isbn)
        self.store[isbn] = price

    def check_if_full_and_remove_excess(self):
        if len(self.store) > self.capacity:
            self.store.popitem(last=False)
