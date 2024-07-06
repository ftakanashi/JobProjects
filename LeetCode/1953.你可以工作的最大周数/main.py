#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_job = max(milestones)
        rest = sum(milestones) - max_job

        if max_job <= rest + 1:
            return sum(milestones)
        else:
            return rest * 2 + 1