#!/usr/bin/env python
from typing import List

class Solution:
    def getStartOne(self, num):
        '''
        用于统计某个8比特字节开头有几个连续的1
        '''
        for i in range(7, -1, -1):
            if num & (1 << i) == 0:
                return 7 - i
        return 8

    def validUtf8(self, data: List[int]) -> bool:
        for num in data:    # 大于255数字一旦出现就是非法，直接False
            if num > 255: return False

        i = 0
        while i < len(data):    # 开始扫描
            digits = self.getStartOne(data[i])    # 扫描每个字符的开头字节的开头连续1个数
            if digits == 0:    # 单字节字符
                i += 1
                continue
            if digits == 1 or digits > 4: return False    # 非法情况
            for d in range(1, digits):    # 合法，检查后面连续的若干个字节是否都是10开头
                if i + d >= len(data) or self.getStartOne(data[i+d]) != 1:
                    return False
            i += digits
        return True