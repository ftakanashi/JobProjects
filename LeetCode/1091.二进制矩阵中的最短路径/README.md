## 题目描述
给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。

二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
```
路径途经的所有单元格都的值都是 0 。
路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
畅通路径的长度 是该路径途经的单元格总数。
```
示例 1：
```
输入：grid = [[0,1],[1,0]]
输出：2
```
示例 2：
```
输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4
```
示例 3：
```
输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1
```

提示：
```
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] 为 0 或 1
```

### 解法 BFS
一眼BFS。只不过相比于比较经典的二维矩阵BFS，这题中的方向是8个而不是上下左右四个。

这个变化看起来好像只需要在进行BFS探索的时候增加几个direction就可以了，但是实际上却没那么简单。
下面是我第一次写的BFS的核心部分代码：
```python
        while queue:
            x, y, step = queue.popleft()
            if x == n - 1 and y == n - 1:
                return step
            seen.add((x, y))
            for a, b in direcs:
                nx, ny = x + a, y + b
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if (nx, ny) in seen: continue
                if grid[nx][ny] == 1: continue
                queue.append((nx, ny, step + 1))
```
看起来并没有什么毛病，但是超时了。

原因在于基于`seen`判断元素是否可行的时机。
可以看到，判断某个格子是否已经走过的判断在最下面做出。
而对于某个格子来说，其上一步的格子可能会有很多（8个方向），
就导致某个时刻时，队列中可能会有很多这个格子的坐标。
然而由于这个格子可能并不是通向终点路径中的一个节点，其实只要探索一次就行了。按照这样的算法会被探索好多次从而浪费了很多时间。

优化方法也很简单，将seen的判断放在最上面，即
```python
x, y, step = queue.popleft()
if (x, y) in seen: continue
```

这样即便队列中有很多重复的无效坐标，在第一次出现时遍历过后，后面就不用重复劳动了。