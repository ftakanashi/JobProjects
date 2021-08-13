#!/usr/bin/env python
from typing import List
from collections import defaultdict, deque

class WordMap:
    def __init__(self):
        self.map = {}
        self.i = 0

    def addWord(self, word):
        if word not in self.map:
            self.map[word] = self.i
            self.i += 1
        return self.getWord(word)

    def getWord(self, word):
        if word in self.map:
            return self.map[word]
        return -1

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 构建word_map
        word_map = WordMap()
        word_map.addWord(beginWord)
        for word in wordList:
            word_map.addWord(word)
        if word_map.getWord(endWord) == -1: return 0    # 如果endWord不在word_map里，那么不可达，直接返回

        # 构建图的同时生成虚拟节点并将其入图
        graph = defaultdict(list)
        cur_words = list(word_map.map.keys())
        for word in cur_words:
            chars = list(word)
            from_i = word_map.getWord(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = '*'
                to_i = word_map.addWord(''.join(chars))    # 添加虚拟节点
                chars[i] = tmp

                # 构建图
                graph[from_i].append(to_i)
                graph[to_i].append(from_i)

        # BFS
        queue = deque()
        start, end = word_map.getWord(beginWord), word_map.getWord(endWord)
        queue.append((start, 0))
        seen = set()
        while queue:
            node, dist = queue.popleft()
            if node == end: return dist // 2 + 1    # 最后别忘去除虚拟节点的额外步数
            if node in seen: continue
            seen.add(node)
            for nxt in graph[node]:
                queue.append((nxt, dist + 1))
        return 0