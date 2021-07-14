#!/usr/bin/env python

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
            self.data[key].append((timestamp, value))
        else:
            self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data: return ''
        info = self.data[key]
        l, r = 0, len(info) - 1
        while l <= r:
            mid = (l + r) // 2
            t, v = info[mid]
            if t == timestamp: return v
            if t < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return info[r][1] if r >= 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)