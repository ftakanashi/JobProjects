#!/usr/bin/env python
class Solution:
    def analyze(self, part):
        i = 0
        if part[0] != "-":
            part = "+" + part
        items = []
        while i < len(part):
            sym = 1 if part[i] == "+" else -1
            i += 1
            is_var, num = False, ""
            while i < len(part) and part[i] not in "+-":
                num += part[i]
                if part[i] == "x": is_var = True
                i += 1

            if is_var:
                items.append((is_var, sym * int(1 if len(num) == 1 else num[:-1])))
            else:
                items.append((is_var, sym * int(num)))
        return items

    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        left = self.analyze(left)
        right = self.analyze(right)
        x_nums, c_nums = [], []
        for is_var, num in left:
            if is_var:
                x_nums.append(num)
            else:
                c_nums.append(-num)
        for is_var, num in right:
            if is_var:
                x_nums.append(-num)
            else:
                c_nums.append(num)

        a = sum(x_nums)
        b = sum(c_nums)

        if a == b == 0:
            return "Infinite solutions"
        elif a == 0:
            return "No solution"
        else:
            return f"x={b // a}"