## 题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：

![](https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png)

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

![](https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png)

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
还需要返回链表中的第一个节点的指针。

### 解法 递推中序遍历
最终返回的双向链表是有序的，又因为给出的树是二叉搜索树，显然可以通过二叉树的中序遍历来做。

更具体的，在遍历到节点`node`时，应该需要保证其与前一个被遍历了的节点`prev`间要有如下操作：
```python
prev.right = node
node.left = prev
prev = node
```
若采用递归方案，那么node就要跨递归层级传递，有点不方便，因此这里采用递推方案。
顺便也复习一下递推的二叉树中序遍历怎么写：

```python
def midorder(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        print(node)    # 操作节点
        root = node.right 
```

此外注意到这样遍历完成之后中间部分的链接都可以了，但是第一个节点的left和最后一个节点的right都还没有连到彼此。

反正链表构建地也差不多了，那干脆从头到尾扫描到最后一个节点，然后手动连接一下两者即可。