import sys

def process(grid):
    m, n = len(grid), len(grid[0])
    direcs = [(0,1), (0,-1), (1,0), (-1,0)]

    def dfs(x, y):
        grid[x][y] = 2
        for a, b in direcs:
            nx, ny = x+a, y+b
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                dfs(nx, ny)

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                ans += 1
    return ans


def main():
    lines = sys.stdin.read().strip().split('\n')
    grid = []
    for l in lines:
        grid.append([int(num) for num in l.strip().split(',')])

    res = process(grid)
    print(res)

main()