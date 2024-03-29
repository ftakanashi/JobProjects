## 题目描述
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。


示例：
```
输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
```
```
提示：如果 h 有多种可能的值，h 指数是其中最大的那个。
```

### 解法 堆
这题解法思路有很多种。

找出一个最大的n，使得数组中大于等于n的数至少有n个。
一个最朴素的想法就是从1开始试，直到n为止。

另一方面，注意到，只要找出数组中最大的值，只要其大于等于1，则答案至少是1；
找出数组中次大的值，只要其大于等于2，答案就至少是2；
以此类推。

于是我们想到排序数组，然后从后往前扫描。比如示例`0 1 3 5 6`。
对于6，大于等于1，所以`ans += 1`
对于5，大于等于2，`ans += 1`
对于3，大于等于3，`ans += 1`
对于1，不大于等于4，因此停止扫描。

以上算法是`O(nlogn + n)`。
改变为用堆来做的话，建堆+不断pop数可以优化到`O(n + hlogn)`。