#!/usr/bin/env python
from typing import List

from collections import Counter, deque

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for cpdomain in cpdomains:
            cnt, domains = cpdomain.split()
            cnt = int(cnt)
            domains = deque(domains.split("."))

            while len(domains) > 0:
                counter[".".join(domains)] += cnt
                domains.popleft()

        ans = []
        for key, cnt in counter.items():
            ans.append(f"{cnt} {key}")
        return ans