#!/usr/bin/env python

from collections import Counter

class Solution:
    num_map = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    def filter(self, counter, feat, num):
        '''
        :param counter: 总的s的计数器
        :param feat: 数字的特征字母
        :param num: 数字本身
        :return:
        '''
        if feat not in counter: return []    # 剩余字母中无法凑出哪怕一个num时
        times = counter[feat]
        for ch in self.num_map[num]:
            counter[ch] -= times
            if counter[ch] == 0:
                counter.pop(ch)
        return [num for _ in range(times)]

    def originalDigits(self, s: str) -> str:
        ans = []
        counter = Counter(s)
        for feat, num in [('z', 0), ('w', 2), ('u', 4), ('x', 6), ('g', 8), ('o', 1),  ('t', 3), ('f', 5), ('v', 7), ('i', 9)]:
            ans.extend(self.filter(counter, feat, num))
        return ''.join([str(num) for num in sorted(ans)])