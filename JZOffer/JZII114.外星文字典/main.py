#!/usr/bin/env python
from typing import List

class Solution:
    def dumpWords(self, graph, word1, word2):
        '''
        对比词对。顺便返回一个bool量。
        进入此方法时我们保证于原词表中，word1在word2前面。
        当通过比对发现word1比word2的字典序更靠后时（比如word2是word1前缀的情况等）就返回False，否则返回True
        '''
        i = j = 0
        flag = False
        while i < len(word1) and j < len(word2):
            ch1, ch2 = word1[i], word2[j]
            if ch1 not in graph: graph[ch1] = set()
            if ch2 not in graph: graph[ch2] = set()
            if ch1 != ch2:
                if ch1 not in graph: graph[ch1] = set()
                graph[ch1].add(ch2)
                flag = True
                break

            i += 1
            j += 1

        # 此时虽然已经得到了某两个字母的前后关系，但是为了图的完整性要将两个单词中剩余字母也都放入图内
        while i < len(word1):
            if word1[i] not in graph: graph[word1[i]] = set()
            i += 1
        while j < len(word2):
            if word2[j] not in graph: graph[word2[j]] = set()
            j += 1

        return flag or len(word1) <= len(word2)

    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        if n == 1: return words[0]    # 特殊情况的处理

        # 开始构建图
        graph = {}
        for i in range(n):
            wa = words[i]
            for j in range(i + 1, n):
                wb = words[j]
                if not self.dumpWords(graph, wa, wb):
                    return ""

        # print(graph)
        # 注意，此时graph内有可能是有值是空集的字母的。
        # 这些字母是游离于连通分量外的独立节点，而在拓扑排序中他们放在哪都不影响

        # 开始拓扑排序，记得有环时无拓扑排序，返回False
        res, visisted, finished = [], set(), set()
        def dfs(node):
            if node in finished: return True
            if node in visisted: return False
            visisted.add(node)
            for nxt in graph[node]:
                if not dfs(nxt): return False
            res.append(node)
            finished.add(node)
            return True

        for ch in list(graph.keys()):
            if not dfs(ch): return ""

        return "".join(reversed(res))    # 最后别忘了拓扑排序的结果数组要倒序才是排序结果