## 题目描述
给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。

示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/28/1483_ex1.png)
```
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
```
示例 2：
```
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19
```

提示：
```
树中节点数目在范围 [1, 104] 之间。
1 <= Node.val <= 100
```

### 解法 层序遍历
不解释…
维护一个`last_layer`数组，遍历每层时实时将层总和加进去，若下面还有则直接将其清零重新计数即可。