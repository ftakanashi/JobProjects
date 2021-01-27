#!/usr/bin/env python
from typing import List

import collections
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        m = collections.OrderedDict()
        m[3] = 'Fizz'
        m[5] = 'Buzz'
        res = []
        for num in range(1, n+1):
            s = ''
            for m_num, m_s in m.items():
                if num % m_num == 0:
                    s += m_s
            if s == '': s = str(num)
            res.append(s)
        return res