#!/usr/bin/env python
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False    # 就这道题而言，不用实现end机制，这里加上是为了方便记忆

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie()
        for word in words:
            node = root
            for ch in reversed(word):    # 单词倒着入字典树
                if ch not in node.children:
                    node.children[ch] = Trie()
                node = node.children[ch]
            node.end = True

        def dfs(node, path):    # dfs统计路径总和
            if len(node.children) == 0: return path
            res = 0
            for child in node.children:
                res += dfs(node.children[child], path + 1)
            return res

        return dfs(root, 1)    # 初始化的path值就是1，因为压缩串要计入#，所以可以把root视作是#的节点