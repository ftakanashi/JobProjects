#!/usr/bin/env python

class Solution1:
    def canTransform(self, start: str, end: str) -> bool:
        # 先是两个简单的判断
        if len(start) != len(end): return False
        if "".join([ch for ch in start if ch != "X"]) != "".join([ch for ch in end if ch != "X"]):
            return False

        # 收集start以及end中所有L和R的下标
        start_L, start_R = [], []
        end_L, end_R = [], []
        n = len(start)
        for i in range(n):
            if start[i] == "L":
                start_L.append(i)
            elif start[i] == "R":
                start_R.append(i)
            if end[i] == "L":
                end_L.append(i)
            elif end[i] == "R":
                end_R.append(i)

        # 开始检查去除X后start和end中同位置的L和R，在原串中是否符合下标的关系条件
        for s, e in zip(start_L, end_L):
            if s < e: return False
        for s, e in zip(start_R, end_R):
            if s > e: return False

        # 经过所有检查都OK，那么就是True了
        return True

class Solution2:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]: return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j: return False
                i += 1
                j += 1

        # 记得遍历完所有剩余字符是否都是X
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1

        return True