#!/usr/bin/env python
from functools import lru_cache as cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        @cache    # 由于erase函数也是接收字符串且不依赖外部信息就可运行，因此也可以做一个cache
        def erase(curr_board):
            '''
            接收一个插入球后的面板情况
            根据消消乐游戏规则对其进行球的消除，返回消除后的情况
            '''
            stack = []
            i = 0
            n = len(curr_board)
            while True:    # 一开始这里写了i < n，但是处理会比较繁琐，不如直接True，然后循环体内安排break更方便
                # 一旦序列符合这个条件，就进行消除
                if len(stack) >= 3 and stack[-3] == stack[-2] == stack[-1]:
                    ch = stack[-1]    # 以当前栈顶为基准
                    while stack and stack[-1] == ch: stack.pop()    # 消除左侧已经入栈的部分
                    while i < n and curr_board[i] == ch: i += 1    # 消除右侧还未入栈但是实际上也会被消除的部分
                if i >= n: break
                stack.append(curr_board[i])
                i += 1
            return ''.join(stack)

        @cache
        def dfs(curr_board, curr_hand):
            '''
            接收某个board情况和当前手里球的情况作为输入
            返回从上述情况出发时，最终到达清空面板时手里能剩下球的数量
            '''
            if curr_board == '': return len(curr_hand)
            if curr_hand == '': return -1
            ans = -1
            m, n = len(curr_board), len(curr_hand)
            for i in range(m + 1):    # 遍历每个插入点位置
                for j in range(n):    # 遍历手中的每个球进行插入
                    new_board = erase(curr_board[:i] + curr_hand[j] + curr_board[i:])
                    ans = max(ans, dfs(new_board, curr_hand[:j]+curr_hand[j+1:]))
                    # 因为返回的是剩下球的数量，因此越多越好，所以用max
            return ans

        rest = dfs(board, hand)
        return (len(hand) - rest) if rest >= 0 else -1