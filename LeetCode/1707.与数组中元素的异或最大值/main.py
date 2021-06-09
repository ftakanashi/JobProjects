#!/usr/bin/env python
from typing import List

BIT = 30

class Trie:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.min_v = float('inf')

class Solution:
    def buildTree(self, nums: List[int]):
        '''
        构建字典树
        '''
        root = Trie()
        for n in nums:

            node = root
            for bit in range(BIT - 1, -1, -1):
                b = (n >> bit) & 1
                if b == 0:
                    if node.left is None: node.left = Trie()
                    node = node.left
                else:
                    if node.right is None: node.right = Trie()
                    node = node.right

                node.min_v = min(node.min_v, n)    # 别忘了把min_v实时维护进去

        return root

    def getMax(self, trie: Trie, x: int, m: int):
        node = trie
        target = 0
        for bit in range(BIT - 1, -1, -1):
            b = (x >> bit) & 1
            if b == 0:
                if node.right and node.right.min_v <= m:
                    node = node.right
                    target = target | (1 << bit)
                elif node.left and node.left.min_v <= m:
                    node = node.left
            else:
                if node.left and node.left.min_v <= m:
                    node = node.left
                elif node.right and node.right.min_v <= m:
                    node = node.right
                    target = target | (1 << bit)

            if node.min_v > m: return -1    # early stopping

        return x ^ target

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        root = self.buildTree(nums)
        answers = []
        for x, m in queries:
            answers.append(self.getMax(root, x, m))
        return answers