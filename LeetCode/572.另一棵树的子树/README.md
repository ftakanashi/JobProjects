## 题目描述
给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

示例 1：
```
输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
```
示例 2：

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)
```
输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
```

提示：
```
root 树上的节点数量范围是 [1, 2000]
subRoot 树上的节点数量范围是 [1, 1000]
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
```

### 解法 双层DFS
这个方法效率不高，不过很直观。

外层DFS是依次扫描root树中的各个子节点。
内层DFS则是接收分别指向root树中的某个节点和subRoot，然后依次扫描。

当内层DFS可以保证两边每个节点都完全一致，自然就可以返回True了。
否则，则需要返回False并返回到外层DFS。

而外层DFS，当以某个node为基准扫描返回False之后，则需要扫描其左子或者右子节点。
两种选择中只要有一种是True就可以返回True。

理清思路后，剩下只需要仔细想想停止递归的条件即可。