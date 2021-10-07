#!/usr/bin/env python

class Solution1:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'

        chars = '0123456789abcdef'
        if num > 0:    # 正数直接进制转换
            res = ''
            while num > 0:
                res = chars[num % 16] + res
                num = num // 16
            return res

        binary = []
        num = -num
        while num > 0:    # 求负数绝对值的二进制表达，注意binary是逆序的
            binary.append(num & 1)
            num = num >> 1
        while len(binary) < 32: binary.append(0)    # 补齐高位0
        binary[-1] = 1    # 最高位置1
        for i in range(31): binary[i] = binary[i] ^ 1    # 取反
        for i in range(31):    # +1 （带进位处理）
            binary[i] = binary[i] ^ 1
            if binary[i] == 1: break

        res = ''
        for i in range(0, 32, 4):
            v = sum(map(lambda x:x[0]*x[1], zip(binary[i:i+4], (1, 2, 4, 8))))    # 4位一组输出十六进制
            res = chars[v] + res
        return res

class Solution2:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'

        chars = '0123456789abcdef'
        res = ''
        for _ in range(8):
            res = chars[num % 16] + res
            num = num // 16
            if num == 0: break
        return res