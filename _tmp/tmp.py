#!/usr/bin/env python
from functools import lru_cache as cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        @cache
        def erase(curr_board):
            stack = []
            i = 0
            n = len(curr_board)
            while True:
                if len(stack) >= 3 and stack[-3] == stack[-2] == stack[-1]:
                    ch = stack[-1]
                    while stack and stack[-1] == ch: stack.pop()
                    while i < n and curr_board[i] == ch: i += 1
                if i >= n: break
                stack.append(curr_board[i])
                i += 1
            return ''.join(stack)

        @cache
        def dfs(curr_board, curr_hand):
            print(curr_board, curr_hand)
            if curr_board == '': return len(curr_hand)
            if curr_hand == '': return -1
            ans = -1
            m, n = len(curr_board), len(curr_hand)
            for i in range(m + 1):
                for j in range(n):
                    new_board = erase(curr_board[:i] + curr_hand[j] + curr_board[i:])
                    ans = max(ans, dfs(new_board, curr_hand[:j]+curr_hand[j+1:]))
            return ans

        # rest = dfs(board, hand)
        # return (len(hand) - rest) if rest >= 0 else -1
        print(erase("WWGGWWGGBBBGGWWGW"))

if __name__ == '__main__':
    s = Solution()
    board = "WWGGGGWW"
    hand = "WRBRW"
    s.findMinStep(board, hand)