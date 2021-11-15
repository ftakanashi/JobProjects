#!/usr/bin/env python
from collections import defaultdict

class MapSum:

    def __init__(self):
        self.map = {}
        self.presum = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        if key not in self.map:
            self.map[key] = val
            for i in range(1, len(key) + 1):
                self.presum[key[:i]] += val
        else:
            tmp = self.map[key]    # 如果是insert修改已有值的情况，那么presum内所有前缀对应值要先减去原值再加上新值
            self.map[key] = val
            for i in range(1, len(key) + 1):
                self.presum[key[:i]] += (val - tmp)

    def sum(self, prefix: str) -> int:
        return self.presum[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)