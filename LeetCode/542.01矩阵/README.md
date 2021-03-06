## 题目描述
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 
 

示例 1：
```
输入：
[[0,0,0],
 [0,1,0],
 [0,0,0]]

输出：
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```
示例 2：
```
输入：
[[0,0,0],
 [0,1,0],
 [1,1,1]]

输出：
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

提示：
- 给定矩阵的元素个数不超过 10000。
- 给定矩阵中至少有一个元素是 0。
- 矩阵中的元素只在四个方向上相邻: 上、下、左、右。

### 解法1 BFS
一般我们感觉DFS好像比BFS更加通用一些。
但是实际上有些时候，比如这道题，BFS比DFS好用的多。

这题如果用DFS，思路应该是从一个点开始探索其上下左右位置，找出其中最小值+1作为本位置的值。
这里的问题就在于，某些情况下这四个值不全。
比如我是从左只有从上至下进行扫描每个位置作为DFS的起点的。
那么DFS探索到`i, j`位置时，显然只有`i - 1, j`和`i, j-1`的值是靠谱的。如果取这两者的最小值，而忽略另两个方向，
可能后来另两个方向的值更小，这样就还要回过头来改`i, j`的值，很麻烦。

一个可行的方案好像是从四个角开始，DFS四次，这样可以确保所有位置都可以碰到最小值。
类似这种思想在解法2的DP中呈现。这里先说更加优雅的BFS。

对于原矩阵中的一个0，其周围一圈1的距离值是1，再往外一圈又都是2，以此类推。
当然，两个0的势力范围如果交集了，那么就要取其中小的值。

事实上，如果我优先把所有0周围探索完了，再开始探索距离为1的那些1，再探索距离为2的那些1，依次类推。
这样是可以保证每个位置最早的时候都被离其最近的0开始的探索包括了。

这个过程其实就是一个BFS。这个任务天然适合BFS。

算法是这样的：
在BFS的队列基础上再维护一个visited，保证每个位置只被处理一次。
从队列中取出一个位置`i, j`后，探索其上下左右四个位置，在不越界同时也没有visit过的情况下，
设置这个新位置的距离值为`i, j`距离值+1。

**多说一句，这种多源点最短路径探索，更一般的其实可以看做是从一个超级源点连接了所有源点，然后从超级源点开始探索的问题。
这种问题天生适合BFS。因为如果要DFS的话你还得想办法如何构造一个超级源点。但是BFS就很符合直觉。直接将所有源点加入队列，相当于默认基于超级源点
的遍历已经结束了。**

### 解法2 DP
如果这题题目改成，找下标小于当前位置最近的0的距离，即只找左方和上方的0的话，就不麻烦了。
只要从左到右从上到下遍历各个位置并且实时维护DP。

DP的状态转移方程是，对于位置`i, j`
如果`matrix[i][j] == 0`，那么`dp[i][j] = 0`，
否则`dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1`。

只是现在没有方向限制，所以作为补偿，遍历四遍。

四遍分别找
- 左方上方
- 左方下方
- 右方上方
- 右方下方

的最近距离0，取四个方向中最小的。

这个方法代码直接抄了答案。