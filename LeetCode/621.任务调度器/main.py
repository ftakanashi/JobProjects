#!/usr/bin/env python
from typing import List

import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        time = 0
        while len(counter) > 0:
            state = counter.most_common()
            for i in range(n + 1):
                if i < len(state):
                    counter[state[i][0]] -= 1
                    if counter[state[i][0]] == 0:
                        del counter[state[i][0]]
                time += 1
                if len(counter) == 0: break

        return time