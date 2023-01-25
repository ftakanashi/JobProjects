#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {k: v for k, v in knowledge}
        key = ""
        for ch in s:
            if ch == "(":
                key = ""
            elif ch == ")":
                v = knowledge.get(key, "?")
                s = s.replace("({})".format(key), v)
                key = ""
            elif key:
                key += ch
        return s