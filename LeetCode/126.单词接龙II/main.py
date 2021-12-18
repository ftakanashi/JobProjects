#!/usr/bin/env python
from typing import List
from collections import deque, defaultdict

class Solution1:
    '''
    整体而言是一个比较暴力的做法。建议优化。
    '''

    def isLinked(self, word1: str, word2: str) -> bool:
        '''
        判断两个单词是否是相邻节点
        '''
        flag = True
        for i in range(len(word1)):
            if word1[i] == word2[i]: continue
            elif flag: flag = False
            else: return False
        return flag is False

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 构建图
        graph = defaultdict(list)
        n = len(wordList)
        for word in wordList:
            if self.isLinked(beginWord, word):
                graph[beginWord].append(word)
                graph[word].append(beginWord)

        for i in range(n):
            for j in range(i):
                if self.isLinked(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        # 开始BFS
        queue = deque([])
        queue.append((beginWord, (beginWord, )))
        seen = set()
        ans = set()    # 防止重复结果，用set收割路径结果
        min_len = float('inf')
        while queue:
            node, path = queue.popleft()
            if node == endWord:
                min_len = len(path) if len(ans) == 0 else min_len
                if len(path) <= min_len:
                    ans.add(path)
                    continue
                else:
                    break

            seen.add(node)
            for nxt in graph[node]:
                if nxt in seen: continue
                queue.append((
                    nxt,
                    path + (nxt, )
                ))
        return list(ans)