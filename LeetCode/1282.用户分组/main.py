#!/usr/bin/env python
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size2people = {}
        for i, size in enumerate(groupSizes):
            if size not in size2people:
                size2people[size] = []
            size2people[size].append(i)

        ans = []
        for size, people in size2people.items():
            for i in range(0, len(people), size):
                ans.append(people[i: i + size])
        return ans