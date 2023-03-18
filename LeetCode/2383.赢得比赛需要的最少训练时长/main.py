#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        need_energy = max(0, sum(energy) - initialEnergy + 1)
        need_experience = 0
        for e in experience:
            if initialExperience <= e:
                need_experience += (e - initialExperience + 1)
                initialExperience = e + 1
            initialExperience += e
        return need_energy + need_experience