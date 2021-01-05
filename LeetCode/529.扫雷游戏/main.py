#!/usr/bin/env python
from typing import List

import collections

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        direc = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,-1),(1,1),(-1,1),(-1,-1)
        ]

        def count_mine(x: int, y: int) -> int:
            count = 0
            for a, b in direc:
                if 0 <= x + a < m and 0 <= y + b < n and board[x+a][y+b] == 'M':
                    count += 1
            return count

        def dfs(x: int, y: int):
            if board[x][y] in 'B123456789':
                return
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return

            mine_count = count_mine(x, y)
            if mine_count > 0:
                board[x][y] = str(mine_count)
                return

            board[x][y] = 'B'
            for a, b in direc:
                if 0 <= x + a < m and 0 <= y + b < n and board[x+a][y+b] == 'E':
                    dfs(x+a, y+b)

        click_x, click_y = click
        dfs(click_x, click_y)
        return board


class Solution2:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        direc = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,-1),(1,1),(-1,1),(-1,-1)
        ]

        def count_mine(x: int, y: int) -> int:
            count = 0
            for a, b in direc:
                if 0 <= x + a < m and 0 <= y + b < n and board[x+a][y+b] == 'M':
                    count += 1
            return count

        queue = collections.deque([])
        queue.append(click)

        while len(queue) > 0:
            x, y = queue.popleft()
            if board[x][y] in 'B123456789':    # 这个优化一定要有，要不然会超时。可能是因为会有大量重复的格子被加入到队列中。
                continue
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif (mine_count:=count_mine(x, y)) > 0:
                board[x][y] = str(mine_count)
            else:
                board[x][y] = 'B'
                for a, b in direc:
                    if 0 <= x + a < m and 0 <= y + b < n and board[x+a][y+b] == 'E':
                        queue.append([x+a, y+b])

        return board