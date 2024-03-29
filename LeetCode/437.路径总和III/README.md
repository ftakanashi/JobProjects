## 题目描述
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例 1：
![](https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg)

```
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
```
示例 2：
```
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
```

提示:
```
二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 
```

### 解法 DFS
这题虽然一看就知道可以用DFS做，但是仔细一想还是稍微有点复杂的。
复杂的点就在于，路径的起始和终点是完全自由的。

这就导致了这里的DFS，其实有两层含义。
第一层，是一般的DFS各个节点，将各个节点作为根节点去遍历。
第二层，是应用的DFS，即递归地计算某个节点为根节点的子树中，总共有几条从根节点出发的路径满足题目要求。

一开始我试图将两层DFS整合在一个dfs函数中完成，但是试了下之后发现有些难。
于是看了答案……（话说每日一题好久都没有看答案才能做出来的了，不知不觉间自己也成长了一些啊

其实可以将两层DFS分开来实现。
代码中的dfs函数，其实是实现了上述第二层，即应用方面的DFS。输入一个节点`node`与到达这个节点前部分路径的总和`s`，接着判断若`node.val + s == targetSum`，
那么说明找到一条路径，结果值加1。

注意这里不能直接返回，因为题目明确说路径的终点不一定是叶子节点，换言之，还应该继续往下遍历搜索。
继续往下搜索就是简单的`res += dfs(node.left, s + node.val)`以及相关右子树的处理了。

在解决第二层DFS后，再回头看第一层DFS。
这里当然可以再定义另一个dfs函数用来做这层DFS。但是一个更简便的办法是直接利用解答方法`self.pathSum`进行递归。

换言之，通过`res = dfs(root, 0)`可以获得以root为根节点的树的总合法路径数量。
这个基础上再加上`self.pathSum(root.left, targetSum)`和`self.pathSum(root.right, targetSum)`，就是最终答案了。
不用担心诸如`root.left.left/right`怎么办，这个解答方法已经被改造成递归，在`self.pathSum(root.left, targetSum)`中就已经自动递归地处理那些子问题了。

上述DFS做法会存在一些重复计算，其实这题也可以通过路径的前缀和的手法来降低复杂度。这了就不赘述了，看答案吧。