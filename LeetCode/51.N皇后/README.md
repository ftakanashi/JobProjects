## 题目描述
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：
![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
```
示例 2：
```
输入：n = 1
输出：[["Q"]]
```
提示：
- 1 <= n <= 9
- 皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。


### DFS回溯法
这里再说下DFS和回溯法的微妙的区别。
DFS模式就是整一个递归函数，在已经解决一部分问题，剩余一部分没解决还需要探索的情况下，传递已经解决部分问题的答案到函数中，并且基于此
递归地探索剩余问题的答案。

一般DFS通常探索到一个答案就完事了。
但是一些场景比如这道题要求所有答案，这就意味着探索完一个答案之后，还要继续探索。
此时可能要重置那些最后被解决的部分问题为未解决状态。

回溯法的模板通常是这样的感觉：
```text
while 一个循环:
    做一些探索的准备操作
    dfs()递归探索
    还原上面的准备操作
```

具体到这道题，我们可以按行扫描放皇后，这样至少保证了每行肯定只有一个皇后。
然后扫描每列，放置到某个位置上必须保证这个位置同列和同左上右下方向斜线和同左下右上方向斜线没有重复的皇后。

上述条件可以通过设置三个集合实现。
已有皇后的列位置集合最方便，就直接让列下标入集合即可。
至于两种斜线方向，其实左下右上斜线方向是指横纵坐标的和`i + j`相等。
左上右下斜线方向是指横纵坐标差`i - j`相等（注意差可能是负数）。

有了这些前提之后，写代码其实并不难了。
由于输出的是模拟的棋盘，为了方便，探索的时候可以先记录每行皇后的列号，
最后额外安排一个函数将所有列号转化为一个棋盘。