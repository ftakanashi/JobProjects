## 题目描述
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树
```
    1
   / \
  2   5
 / \   \
3   4   6
```
将其展开为：
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

### 解法 先根序DFS
题意比较模糊。一开始以为只要展开成一个链表就行了。

但是观察输出输入之间的关系，可以发现，其实是要求把树按照先根序，展开成一个每个节点都是父节点的右子节点的链表。

对，最最重要的是要意识到，展开之后的每个节点仍然是TreeNode类实例而不是ListNode。
因此没有next属性，相反有left和right属性。

意识到这一点，写代码就不难了。