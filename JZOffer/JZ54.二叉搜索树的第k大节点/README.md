## 题目描述
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
```
示例 2:
```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
```

### 解法 中序遍历
显然，根据二叉搜索树的性质，通过中序遍历就可以得到各个节点值的排序顺序了。

注意这里求的是第k 大 的数，所以遍历的时候要先处理右子树再处理左子树。

另外，递归方法的遍历不是不能做，只是需要维护一个全局的count变量以及res结果容器。
这两者通常可以通过类变量之类的办法来实现。
然而在得到结果后递归方法还是无法提前返回，要等所有遍历完成后才行。

因此，这里采用递推的方法。顺便也复习一下递推中序遍历的写法。