#!/usr/bin/env python
from typing import List

import random
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.bound = m * n - 1
        self.map = {}

    def flip(self) -> List[int]:
        n = self.n
        pos = random.randrange(self.bound + 1)

        if pos in self.map:
            real_pos = self.map[pos]
            ans = [real_pos // n, real_pos % n]
        else:
            ans = [pos // n, pos % n]

        if self.bound in self.map:
            self.map[pos] = self.map[self.bound]
        else:
            self.map[pos] = self.bound
        # 上面两个if/else分支都可以用get等方法更加简化一些。这里为了代码容易懂，没有简化

        self.bound -= 1
        return ans

    def reset(self) -> None:
        self.bound = self.m * self.n - 1
        self.map.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()