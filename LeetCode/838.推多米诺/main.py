#!/usr/bin/env python

from collections import deque
class Solution1:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        queue = deque()
        for i, d in enumerate(dominoes):    # 初始化队列
            if d != ".": queue.append((i, d))

        while queue:
            changed = set()    # 一轮内修改过的位置全用这个哈希集记录下来
            for _ in range(len(queue)):
                pos, direc = queue.popleft()

                if direc == "L" and pos > 0:
                    tgt = pos - 1
                    if dominoes[tgt] == ".":
                        dominoes[tgt] = "L"
                        changed.add(tgt)
                        queue.append((tgt, "L"))
                    elif dominoes[tgt] == "R" and tgt in changed:    # 若本位置左边是R，但是这个R是本轮早些时候的操作修改过来的，那么说明其收到了两边的力，应该保持直立，所以修正回"."
                        dominoes[tgt] = "."

                elif direc == "R" and pos < n - 1:
                    tgt = pos + 1
                    if dominoes[tgt] == ".":
                        dominoes[tgt] = "R"
                        changed.add(tgt)
                        queue.append((tgt, "R"))
                    elif dominoes[tgt] == "L" and tgt in changed:
                        dominoes[tgt] = "."

        return "".join(dominoes)

class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        left, right = [float('inf') for _ in range(n)], [float('inf') for _ in range(n)]

        # 顺序遍历
        i = flag = 1
        while i < n:
            if dominoes[i-1] == "R":
                while i < n and dominoes[i] == ".":
                    right[i] = flag
                    flag += 1
                    i += 1
                flag = 1
            i += 1

        # 逆序遍历
        i, flag = n-2, 1
        while i >= 0:
            if dominoes[i+1] == "L":
                while i >= 0 and dominoes[i] == ".":
                    left[i] = flag
                    flag += 1
                    i -= 1
                flag = 1
            i -= 1

        # 最终判断
        res = [ch if ch != "." else "." for ch in dominoes]
        for i in range(n):
            if right[i] < left[i]:
                res[i] = "R"
            elif left[i] < right[i]:
                res[i] = "L"
        return "".join(res)