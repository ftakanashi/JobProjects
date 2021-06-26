#!/usr/bin/env python
import collections

class Solution1:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(101)]
        queue = collections.deque([])
        queue.append((n, 0, len(squares) - 1))
        while len(queue) > 0:
            rest, count, max_i = queue.popleft()
            if rest == 0: return count
            for i in range(max_i, -1, -1):
                if squares[i] > rest: continue
                queue.append((rest - squares[i], count + 1, i))
        return -1

from math import sqrt
class Solution2:
    def numSquares(self, n: int) -> int:

        def is_square(num):
            root = int(sqrt(num))
            return root**2 == num

        def check_answer_4(num):    # num == 4^k * (8m+7)
            while num % 4 == 0:
                num /= 4
            return num % 8 == 7

        if is_square(n): return 1
        if check_answer_4(n): return 4
        for i in range(1, int(sqrt(n)) + 1):
            rest = n - i**2
            if is_square(rest): return 2

        return 3