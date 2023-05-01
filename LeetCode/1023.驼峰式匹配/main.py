#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def check(self, query: str, pattern: str) -> bool:
        i = 0
        for ch in query:
            if i < len(pattern) and pattern[i] == ch:
                i += 1
                # 这里不能加 i == len(pattern) 后 break
                # 因为要考虑比如query是FooBarTest而pattern是FoBa之类的情况，即query有更多节驼峰
            elif ch.isupper():
                return False

        return i == len(pattern)

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.check(q, pattern) for q in queries]