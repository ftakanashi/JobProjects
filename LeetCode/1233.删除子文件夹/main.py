#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # 构造字典树
        root = Trie()
        for path in folder:
            node = root
            for d in path.strip("/").split("/"):
                if d not in node.children:
                    node.children[d] = Trie()
                node = node.children[d]
            node.end = True

        def dfs(node):
            res = []
            for child_str, child_node in node.children.items():
                # 针对每个子节点，首先看end是否是True
                # 若是 则无需进一步扫描，直接返回片段
                if child_node.end:
                    res.append("/" + child_str)
                else:
                    # 若否，则进一步dfs扫描该子节点，查看其是否有更深的子目录
                    #   若有则收割返回的路径，拼接该子节点本身的名称，然后向上返回
                    for suf in dfs(child_node):
                        res.append("/" + child_str + suf)
            return res

        return dfs(root)