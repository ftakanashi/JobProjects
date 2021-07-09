#!/usr/bin/env python
import string
from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        UPPER = set(string.ascii_uppercase)
        LOWER = set(string.ascii_lowercase)
        N = len(formula)
        stack = []
        i = 0
        while i < N:
            ch = formula[i]
            if ch in UPPER:    # 当前位置是一个原子的开头
                # 获得完整的原子表达
                while i+1 < N and formula[i+1] in LOWER:
                    ch += formula[i+1]
                    i += 1
                cnt = 0
                i += 1
                while i < N and formula[i].isdigit():
                    cnt = cnt * 10 + int(formula[i])
                    i += 1
                cnt = max(cnt, 1)    # 一位数字都没有的情况表示系数是1而不是0
                stack.append((ch, cnt))

            elif ch == '(':    # 进入栈统计括号内部内容
                stack.append('(')
                i += 1

            else:
                all_cnt = 0
                while i+1 < N and formula[i+1].isdigit():
                    all_cnt = all_cnt * 10 + int(formula[i+1])
                    i += 1
                all_cnt = max(all_cnt, 1)    # 获取括号整体系数，和获取原子系数类似
                tmp = []
                while stack and stack[-1] != '(':
                    atom, cnt = stack.pop()
                    tmp.append((atom, cnt * all_cnt))
                stack.pop()
                stack.extend(tmp)    # 将系数更新后的原子返回栈
                i += 1

        # 根据栈中内容先构建counter，再基于counter构建答案字符串。
        counter = Counter()
        for atom, cnt in stack:
            counter[atom] += cnt
        res = ''
        for atom in sorted(counter):
            res += f'{atom}{counter[atom]}' if counter[atom] > 1 else f'{atom}'
        return res