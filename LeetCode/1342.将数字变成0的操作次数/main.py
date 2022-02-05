#!/usr/bin/env python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_num = bin(num)[2:]
        return len(bin_num) - 1 + bin_num.count("1")