#!/usr/bin/env python
# -*- coding:utf-8 -*-

import collections
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = []
        self.i_map = collections.defaultdict(set)


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.container.append(val)
        flag = val not in self.i_map
        self.i_map[val].add(len(self.container) - 1)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.i_map[val]) == 0:    # 由于采用了defaultdict，所以无需判断val not in i_map的情况
            return False

        i = self.i_map[val].pop()    # 待删除元素的下标（若有多个默认用最靠后一个，用pop还可以顺便删掉，省得后面再写代码删）
        j = len(self.container) - 1    # 当前最后一个元素

        val_j = self.container[j]
        self.container[i] = val_j    # 最后一个元素覆盖待删除元素
        self.i_map[val_j].add(i)    # 最后一个元素的下标信息同步
        self.i_map[val_j].remove(j)    # 这里的add和remove不能反，当i == j时，j已经不存在，remove(j)报错

        self.container.pop()    # 删除最后一个元素

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.container)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()