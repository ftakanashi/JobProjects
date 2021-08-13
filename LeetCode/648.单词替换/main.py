#!/usr/bin/env python
from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:    # 将所有前缀入字典树
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Trie()
                node = node.children[ch]
            node.end = True

        def search(word):    # 匹配函数，将word的各个字符依次拉入字典树匹配。当匹配到前缀时返回前缀，否则返回None
            node = root
            tmp = []
            for ch in word:
                if node.end or ch not in node.children: break
                node = node.children[ch]
                tmp.append(ch)
            return ''.join(tmp) if node.end else None

        res = []
        for word in sentence.split():
            prefix = search(word)
            res.append(prefix if prefix else word)
        return ' '.join(res)