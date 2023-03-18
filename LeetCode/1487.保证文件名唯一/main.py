#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        used = {}
        for name in names:
            if name not in used:
                used[name] = 1
                ans.append(name)
            else:
                # 由于本次扫描前可能有前序的 `name(x)` 出现（x比当前used[name]更大）
                # 所以需要一个while循环找到那个还没有被使用的序号
                k = used[name]
                while "{}({})".format(name, k) in used:
                    k += 1

                new_name = "{}({})".format(name, k)
                ans.append(new_name)
                used[name] += 1
                used[new_name] = 1    # 别忘了这个

        return ans