#!/usr/bin/env python
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = []
        if expression[0] != "-":
            expression = "+" + expression

        # 解析所有分数
        i = 0
        while i < len(expression):
            minus = expression[i] == "-"
            i += 1

            numerator = 0
            while expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1

            i += 1  # exp[i] is "/"

            denominator = 0
            while i < len(expression) and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1

            nums.append((minus, numerator, denominator))

        # 加和所有分数
        x, y = 0, 1
        for flag, a, b in nums:
            new_y = y * b
            if flag:
                new_x = x * b - y * a
            else:
                new_x = x * b + y * a

            gcd = math.gcd(abs(new_x), new_y)
            if gcd > 1:
                new_x //= gcd
                new_y //= gcd

            x, y = new_x, new_y

        return f"{x}/{y}"