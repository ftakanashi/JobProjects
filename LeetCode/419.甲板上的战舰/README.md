## 题目描述
给你一个大小为 m x n 的矩阵 board 表示甲板，其中，每个单元格可以是一艘战舰 'X' 或者是一个空位 '.' ，返回在甲板 board 上放置的 战舰 的数量。

战舰 只能水平或者垂直放置在 board 上。换句话说，战舰只能按 1 x k（1 行，k 列）或 k x 1（k 行，1 列）的形状建造，其中 k 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。

示例 1：

![](https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg)
```
输入：board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2
```
示例 2：
```
输入：board = [["."]]
输出：0
```

提示：
```
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 是 '.' 或 'X'
```
 
```
进阶：你可以实现一次扫描算法，并只使用 O(1) 额外空间，并且不修改 board 的值来解决这个问题吗？
```

### 解法 一次扫描
刚看到这道题，第一感觉是只能扫描两边分别统计各行有几个战舰，各列又有几个战舰，而且过程中肯定需要用到一些外部的数据结构比如栈之类的。
无论如何都做不到进阶要求。

后来仔细看了一下题目，发现题目给出了限制，两个战舰不相邻，这就大大简化了。

既然不相邻，那么就意味着某个战舰的四周围一定都是空的。又因为战舰是一个长条形的，所以只要扫描到一个格子，
其中值是X，并且有超过两个以上的相邻格子是空的，那么就一定是一个战舰的头或者尾。

我们只需要关注比如战舰的头（我们定义横形战舰的最左边，竖形战舰的最上边是头），扫描一遍所有格子，找出所有战舰头就行了。

考虑到越界的情况，最终扫描判断战舰头的判断条件应该长这样：
```python
board[i][j] == 'X' and \
(i == 0 or board[i-1][j] == '.') and \
(j == 0 or board[i][j-1] == '.')
```
即，只要保证某个值是X的格子，其上方和左方是空格，那么他一定是一个战舰的头。