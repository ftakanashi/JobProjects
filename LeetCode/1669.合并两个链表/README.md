## 题目描述
给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。

请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。

下图中蓝色边和节点展示了操作后的结果：
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/fig1.png)

请你返回结果链表的头指针。

示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex1.png)
```
输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
输出：[0,1,2,1000000,1000001,1000002,5]
解释：我们删除 list1 中下标为 3 和 4 的两个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
```
示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex2.png)
```
输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
解释：上图中蓝色的边和节点为答案链表。
```

提示：
```
3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
```

### 解法 模拟
没什么可说的，就链表模拟就完了…

首先先扫描一遍list1，并进行计数从而得到`a`和`b`之间的节点是哪些。
我们称这部分节点为删除部分。
为了后续处理方便，可以记录删除部分第一个节点的前一个节点以及最后一个节点的后一个节点。

然后再扫描一遍list2，找到list2的最后一个节点。
然后把两边拼接起来即可。

具体逻辑和细节可看代码。
由于题目保证了`a`和`b`的合法性，所以方便了很多，不用判断很多边界情况。