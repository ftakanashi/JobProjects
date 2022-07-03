#!/usr/bin/env python
from typing import List

class Trie:
    def __init__(self):
        self.end = False
        self.children = [None for _ in range(26)]

class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for ch in word:
                chi = ord(ch) - ord("a")
                if node.children[chi] is None:
                    node.children[chi] = Trie()
                node = node.children[chi]
            node.end = True

    def search(self, searchWord: str) -> bool:

        def dfs(node, pos, flag):
            '''
            node: 当前遍历到的字典树节点
            pos: 当前正在扫描的searchWord中的字符的下标
            flag: 开关，用于指示之前是否已经发生过字符的替换
            '''
            if pos == len(searchWord):
                return node.end and not flag
            if flag:
                for i, child in enumerate(node.children):
                    if child is None: continue
                    if dfs(child, pos + 1, searchWord[pos] == chr(ord("a") + i)):
                        return True
            else:
                for i, child in enumerate(node.children):
                    if child is None or searchWord[pos] != chr(ord("a") + i): continue
                    if dfs(child, pos + 1, flag):
                        return True
            return False

        return dfs(self.root, 0, True)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)