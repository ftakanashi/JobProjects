#!/usr/bin/env python
from typing import List

class TrieNode:
    '''
    字典树节点类
    end表示是否有某个单词在本节点结束
    children表示下一个字母的26个可能
    '''
    def __init__(self):
        self.end = False
        self.children = [None for _ in range(26)]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 初始化字典树，并将words中所有单词插入其中
        trie = TrieNode()
        for word in words:
            p = trie
            for ch in word:
                chi = ord(ch) - ord('a')
                if p.children[chi] is None:
                    p.children[chi] = TrieNode()
                p = p.children[chi]
            p.end = True


        m, n = len(board), len(board[0])
        res = set()    # 先用set保存结果
        direcs = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(x, y, seen, p, path):
            '''
            x,y：指当前探索位置的坐标
            seen：一个哈希集，表示该dfs过程中已经探索过的位置的哈希集
            p：字典树指针
            path：当前dfs过程已经探索过位置连成的部分单词
            '''
            if p is None: return    # 说明当前探索过位置连成的词不在字典树中

            if p.end is True:    # 需要收割
                path.append(board[x][y])
                res.add(''.join(path))
                path.pop()
                # 注意这里不要return。因为可能存在'oa', 'oaa'这样的words。探索到第二个a之后先收割oa，接着还需要探索oaa的可能

            seen.add((x, y))
            path.append(board[x][y])
            for a, b in direcs:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                if (nx, ny) in seen: continue
                np = p.children[ord(board[nx][ny]) - ord('a')]
                dfs(nx, ny, seen, np, path)
            seen.remove((x, y))    # 回溯
            path.pop()

        for i in range(m):
            for j in range(n):
                dfs(i, j, set(), trie.children[ord(board[i][j]) - ord('a')], [])

        return list(res)