#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter, deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        counter = Counter(students)

        while sandwiches:
            s = sandwiches[0]
            if counter[s] > 0:
                counter[s] -= 1
                sandwiches.popleft()
            else:
                # 进入到这个分支，就说明当前已经没有学生能和栈顶三明治匹配了
                return counter[s ^ 1]

        return 0