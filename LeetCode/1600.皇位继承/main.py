#!/usr/bin/env python
from typing import List

from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.name2node = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.name2node[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(name):
            if name not in self.dead: res.append(name)
            for child in self.name2node[name]:
                dfs(child)
        dfs(self.kingName)
        return res