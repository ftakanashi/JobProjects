#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = j = k = 0    # i,j是窗口左右边界，k是指向当前窗口内最靠右纯净区域的左边界
        choices = set([])
        prev = None
        max_len = 0
        while j < len(tree):
            if tree[j] in choices or len(choices) < 2:
                choices.add(tree[j])    # 这步对于tree[j] in choice的条件是多余的。为了代码美观整合了两个条件
                if tree[j] != prev:
                    k = j
            else:
                max_len = max(max_len, j - i)
                choices = set([tree[k], tree[j]])
                i, k = k, j    # 左边界收缩到k，而k又恰好是当前的j

            prev = tree[j]
            j += 1

        max_len = max(max_len, j - i)    # j完成整个遍历之后的最后一个窗口没有在循环中获取长度。需要在这里再收割一下。

        return max_len

from collections import Counter
class Solution0:
    def totalFruit(self, fruits: List[int]) -> int:
        i = j = 0
        n = len(fruits)
        bucket = Counter()
        ans = 0
        while j < n:
            bucket[fruits[j]] += 1

            while i < j and len(bucket) > 2:
                f = fruits[i]
                bucket[f] -= 1
                i += 1
                if bucket[f] == 0:
                    bucket.pop(f)

            ans = max(ans, j - i + 1)
            j += 1

        return ans