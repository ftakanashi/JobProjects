#!/usr/bin/env python

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index_map:
            self.list.append(val)
            self.index_map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index_map:
            tail = self.list.pop()
            if len(self.list) > 0 and tail != val:
                i = self.index_map[val]
                self.list[i] = tail
                self.index_map[tail] = i
            del self.index_map[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)