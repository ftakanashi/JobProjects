#!/usr/bin/env python

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            i = key % 10000
            self.data[i].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            i = key % 10000
            self.data[i].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = key % 10000
        return key in self.data[i]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)