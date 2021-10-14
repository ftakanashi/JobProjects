## 题目描述
给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 SummaryRanges 类：
- SummaryRanges() 使用一个空数据流初始化对象。
- void addNum(int val) 向数据流中加入整数 val 。
- int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
 

示例：
```
输入：
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
```

提示：
```
0 <= val <= 104
最多调用 addNum 和 getIntervals 方法 3 * 104 次
```

- 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

### 解法 二分查找
这题其实不用想得太复杂。
首先，摆明了可以用线段树做（虽然我并不会线段树…）。

如果不用线段树，则需要考虑如何在新来一个数后合并区间。
考虑到区间的左端点们和右端点们总是有序排列的，因此可以选择用二分查找。

简言之，目前有区间，新来一个数时，查找其值在左端点们的序列（即`[ranges[0] for range in self.ranges]`）中应该插入的下标位置`low_i`。
同理，还可以得到一个右端点序列中新来数插入的下标位置`high_i`。

基于这两个值，可以做一些分类讨论。
比如，当当前序列是`[1,3], [7,7]`的时候，新来一个`0`,`2`,`5`,`6`,`8`，等等情况分别是怎样的。
具体的讨论细节这里就不说了。简单来说就是
1. 要看插入值是否恰好已经是某个区间内部的值
2. 要看插入值是否能和周边某个或者两个区间相连，从而不增加新区间

在实践过程中，还发现了一个优化点。当区间内有`[1,3]`这个区间时，说明了2这个数字一定在之前出现过。
而实际上，对于数据流中已经出现过的数字，必然已经被囊括在当前区间内，因此完全可以不做处理直接返回。
因此，优化方法就是在类中增加一个`seen`哈希集，用于保存已经出现过的数字。
对于数据流中新来的，但是之前出现过的数字，我们直接return即可。

另外，在进行这个优化之后，发现如果确定新来的数字不是之前出现过的数字，那么其实上面的分类讨论中的第一种情况不存在，可以直接省略。
进而发现，其实没必要求两个下标值。只要求其中一个即可。
这里我们采取了 通过二分，求目标值在左端点序列中的插入位置。
只用讨论目标值与这个位置两侧区间（考虑到最开始和最后的两种特殊情况，也有可能只有一侧区间）是否可相连即可。

按照以上思路写代码即可。有些解释不清的，放在代码注释中了。