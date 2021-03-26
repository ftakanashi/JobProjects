#!/usr/bin/env python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2069
        self.data = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.size
        for j, kv in enumerate(self.data[i]):
            if kv[0] == key:
                self.data[i][j][1] = value
                return

        self.data[i].append([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.size
        for j, kv in enumerate(self.data[i]):
            if kv[0] == key:
                return kv[1]

        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.size
        for j, kv in enumerate(self.data[i]):
            if kv[0] == key:
                self.data[i].pop(j)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)