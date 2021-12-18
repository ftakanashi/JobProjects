#!/usr/bin/env python
from typing import List

from collections import defaultdict
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        n = len(persons)

        # 预处理，将times中每个时间点上得票最多的候选人是谁预处理出来
        self.t2p = [-1 for _ in range(n)]
        cand = None
        votes = defaultdict(int)
        for i in range(n):
            p = persons[i]
            votes[p] += 1
            if votes[p] >= votes[cand]:
                cand = p
            self.t2p[i] = cand

    def q(self, t: int) -> int:
        pos = bisect.bisect(self.times, t) - 1
        return self.t2p[pos]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)