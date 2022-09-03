#!/usr/bin/env python
from typing import List
from sortedcontainers import SortedList

class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False
        self.words = SortedList()

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in products:
            node = root
            for ch in product:
                chi = ord(ch) - ord("a")
                if node.children[chi] is None:
                    node.children[chi] = Trie()
                node = node.children[chi]
                node.words.add(product)
            node.end = True

        ans = []
        node = root
        for ch in searchWord:
            chi = ord(ch) - ord("a")
            child = node.children[chi]
            if child is None:
                break
            node = child
            ans.append(list(node.words[:3]))

        while len(ans) < len(searchWord):
            ans.append([])
        return ans
