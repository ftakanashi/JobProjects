#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n: return []
        p_counter = Counter(p)
        s_counter = Counter(s[:m])
        ans = []
        i = 0
        while i <= n-m:
            if p_counter == s_counter: ans.append(i)
            if i == n-m: break

            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0: s_counter.pop(s[i])

            if s[i+m] not in p_counter:   # 优化点
                i = i + m + 1
                s_counter = Counter(s[i:i+m])
            else:
                s_counter[s[i+m]] += 1
                i += 1
        return ans

from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        ans = []
        if m > n: return ans
        diff = defaultdict(int)
        for i in range(m):
            diff[s[i]] += 1
            diff[p[i]] -= 1
        diff_cnt = [diff[ch] == 0 for ch in diff].count(False)    # 初始状态下值不为0的键值对数量

        for i in range(n-m+1):
            if diff_cnt == 0: ans.append(i)    # 当前差分哈希表中，非零值的键值对数量为0，换言之所有键值对的值都是0，符合要求
            if i == n-m: break

            ch = s[i]    # 从窗口中去除某字母时
            if diff[ch] == 1: diff_cnt -= 1    # 若该字母之前窗口恰好比p多1个，那么此时更新差分后，diff_cnt减去1
            elif diff[ch] == 0: diff_cnt += 1    # 相反的情况，加上1
            diff[ch] -= 1    # 最后别忘了还需要更新差分

            ch = s[i+m]    # 向窗口中添加某字母，逻辑也是类似的
            if diff[ch] == -1: diff_cnt -= 1
            elif diff[ch] == 0: diff_cnt += 1
            diff[ch] += 1

        return ans