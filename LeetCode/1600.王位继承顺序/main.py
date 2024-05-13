#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Node:
    def __init__(self, name):
        self.name = name
        self.dead = False
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.nodeMap = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        parentNode = self.nodeMap[parentName]
        childNode = Node(childName)
        self.nodeMap[childName] = childNode
        parentNode.children.append(childNode)

    def death(self, name: str) -> None:
        self.nodeMap[name].dead = True

    def getInheritanceOrder(self) -> List[str]:
        res = []

        def dfs(node):
            if not node.dead:
                res.append(node.name)
            for child in node.children:
                dfs(child)

        dfs(self.root)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()