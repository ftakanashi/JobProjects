## 题目描述
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
```
输入: 1->2->3->3->4->4->5
输出: 1->2->5
```
示例 2:
```
输入: 1->1->1->2->3
输出: 2->3
```

### 解法1 递归
将方法定义成："去除开头部分的重复项"的方法。
显然，如果head本身是None或者`head.next`是None，就直接返回。

当长度大于1时，需要递归判断。此时，只要判断`head`和`head.next`是否相同。

如果相同，则用一个while循环取出开头的重复部分（至少两个节点），而后返回剩余部分的head。

如果不同，则至少说明当前head节点是应该保留的，因此递归调用函数，输入为`head.next`。

详情见代码。

### 解法2 递推
没啥可说的，就是最普通的思路。
两个游标i,j一前一后从左向右扫描。当碰到`j.val == j.next.val`的情况时让`j`先走。
而后`i.next = j.next`即可。

这里有几个注意点。

首先，因为开头有可能就是重复项，为了保证`i`的独立性，所以需要设立dummy head。

另外，如果上面的`while j.val == j.next.val`循环一次都没进去过，那么此时两个游标都要向前移动一格。
相反，如果进去了上述循环，则在`i.next = j.next`之后，`i`不要动，`j`需要往前走一格。
