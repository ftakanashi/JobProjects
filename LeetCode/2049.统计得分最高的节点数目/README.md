## 题目描述
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。

示例 1:

![](https://assets.leetcode.com/uploads/2021/10/03/example-1.png)
```
输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
```
示例 2：
```
输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。
```

提示：
```
n == parents.length
2 <= n <= 105
parents[0] == -1
对于 i != 0 ，有 0 <= parents[i] <= n - 1
parents 表示一棵二叉树。
```

### 解法 哈希表 DFS
题目意思有好几层，但是每一层的意思倒都不复杂。

简单来说，核心就是给出一个二叉树。

针对这个树中的每个节点，题目要求做如下操作：
将这个节点删除，然后将剩下还能连在一起的各个联通分量做分量内节点的数量计算，然后将这些计数值全部乘起来，
作为"将当前节点删除"能得到的分数。
然后要求统计所有节点中，能够拿到最大分数的节点总共有几个。

由于题目给出的二叉树并不是经典的基于`TreeNode`类的形式，而是一个parents列表，用于表示所有节点的父节点（所有节点都从0到n-1编号），
所以我们的第一步是考虑如何将树表示出来。
一个显而易见的办法是用一个`parent: [node1, node2]`的形式的哈希表。

接着考虑题目中的操作如何实现。
观察一些例子之后发现，删除一个节点后剩余的节点们必然是
- 原该节点左子树
- 原该节点右子树
- 整棵树删去原该节点为根节点的子树

综合来看，只需要知道树中每一个子树的节点数目，上述的每一项都是可以知道的，因此也就很轻松就能求出删除一个节点能获得的分数了。
而这点可以通过DFS搞定。

最后别忘了考虑两种特殊情况，即节点是根节点本身，以及节点是叶子节点的情况。

综上，算法描述如下。
首先，使用一个哈希表表征树。
接着，通过一次DFS，将树中每个子树的节点数量求出，这其中的对应关系也用一个哈希表维护。
接着，遍历所有节点并尝试删除相关节点，计算其分数。
由于遍历过程中尚不知最终的最大分数值是多少，因此只能先将所有分数和计数维护下来。
最终从计数counter中找出最大分数值对应的节点数目。

更多细节写在代码注释中了。