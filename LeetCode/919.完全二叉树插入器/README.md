## 题目描述
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 CBTInserter 类:
```
CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
CBTInserter.get_root() 将返回树的头节点。
```

示例 1：
```
输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]

解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
```

提示：
```
树中节点数量范围为 [1, 1000] 
0 <= Node.val <= 5000
root 是完全二叉树
0 <= val <= 5000 
每个测试用例最多调用 insert 和 get_root 操作 104 次
```

### 解法 队列 层序遍历套路
这题乍一看好像没那么难。
因为最最简单的做法，就是每次insert的时候我都进行一次层序遍历，直到找到完全二叉树中最靠右下角的那个节点（我们称其为tail）。
然后把新节点接上去就可以了。

当然，这么做时间复杂度会比较高。

另一方面，我们可以实时维护这个tail，相当于把找tail这个工作给砸瓦鲁多一下，每接一个新节点后更新一下tail，一点点向前推进。

具体的，在初始化时，我们维护一个`self.tail_q`队列，并且找到初始状态下树的tail，用`self.tail`保存起来。
任何时候，我们保证比`self.tail`更右边更下面的节点都已经按照顺序被保存在`self.tail_q`中。

在insert的时候，首先无脑将新节点加入`self.tail_q`（因为有上面这条保证，所以可以无脑）
然后判断`self.tail`的两个子树的空的情况。
若左子树为空，则新节点接入其左子树，`self.tail`仍然是它，不用更新。
否则，接入右子树，`self.tail`被更新成`self.tail_q`中的下一个元素。

按照以上逻辑写代码即可。
顺便一提，上述做法居然可以100%… 印象中这是我头一次手写出100%…