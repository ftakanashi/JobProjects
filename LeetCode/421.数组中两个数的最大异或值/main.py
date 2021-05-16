#!/usr/bin/env python
from typing import List

class Solution1:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        for bit in range(30, -1, -1):
            pref_nums = [n >> bit for n in nums]
            seen = set(pref_nums)
            possible_x = (x << 1) + 1
            flag = False
            for pref_n in pref_nums:
                if possible_x ^ pref_n in seen:
                    flag = True
                    break
            x = possible_x if flag else possible_x - 1
        return x

class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Solution2:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TreeNode()

        # 构建树
        for n in nums:
            node = root
            for i in range(30, -1, -1):
                bit = (n >> i) & 1
                if bit == 0:
                    if node.left is None: node.left = TreeNode()
                    node = node.left
                else:
                    if node.right is None: node.right = TreeNode()
                    node = node.right

        ans = 0
        # 遍历每个数作为基准，并扫描构建好的字典树
        for n in nums:
            res = 0
            node = root
            for i in range(30, -1, -1):
                bit = (n >> i) & 1
                if (bit == 0 and node.right) or (bit == 1 and node.left):
                    res = (res << 1) + 1
                    node = node.right if bit == 0 else node.left
                else:
                    res = (res << 1)
                    node = node.left if bit == 0 else node.right
            ans = max(ans, res)
        return ans

