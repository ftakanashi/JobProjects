#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.stream = ""
        for word in words:
            node = self.root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = Trie()
                node = node.children[ch]
            node.end = True

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        node = self.root
        for ch in self.stream:
            if node.end: return True
            if ch not in node.children: return False
            node = node.children[ch]
        return node.end    # 注意按照这个算法，结束循环后的node恰好是最后一个字母对应的节点，此时不应直接返回False，而是看这个节点的end值

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)