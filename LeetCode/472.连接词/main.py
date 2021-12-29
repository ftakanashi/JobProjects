#!/usr/bin/env python
from typing import List

class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False

class Solution:
    def insertWord(self, root: "Trie", word: str) -> bool:
        '''
        向字典树中插入某个词
        '''
        assert word
        node = root
        for ch in word:
            ch_i = ord(ch) - ord('a')
            if node.children[ch_i] is None:
                node.children[ch_i] = Trie()
            node = node.children[ch_i]
        node.end = True

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        root = Trie()
        words.sort(key=len)    # 按词长排序

        def dfs(word: str, pos: int) -> bool:
            if pos == len(word): return True
            node = root
            for i in range(pos, len(word)):
                ch_i = ord(word[i]) - ord('a')
                if node.children[ch_i] is None:
                    return False
                if node.children[ch_i].end and dfs(word, i + 1):
                    return True
                node = node.children[ch_i]
            return False

        for word in words:
            if word == "": continue
            if dfs(word, 0):
                ans.append(word)
            else:
                self.insertWord(root, word)
        return ans