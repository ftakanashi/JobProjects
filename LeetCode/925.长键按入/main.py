#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while j < len(typed):
            # 这个循环条件很巧妙。不把i也计入进来，是为了typed比name长的时候，typed末尾的所有字符也要一个个
            # 扫描过去，验证其是否和name的最后一个字符相同
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j - 1] == typed[j]:
                # j > 0是为了避免第一个字符就不同的情况的错误
                j += 1
            else:
                return False

        return i == len(name)