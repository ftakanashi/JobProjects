## 题目描述
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

示例 1：
```
输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
```
示例 2：
```
输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
```

提示：
```
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
```

### 解法 哈希表 模拟
这题看着不难，实际上…也不难。。

因为题目明确了输入数组长度是10000以内，所以不用特别在意低时间复杂度。

最开始，显而易见的，若`hand`的长度无法被`groupSize`整除，那么什么操作都不用做直接False即可。
若可以整除，就需要考虑如何组织各个顺子。
按照一般思路来看，泛泛来说，基于处于边缘的数字统计顺子比处于内部的数字更加保险。
比如示例1，如果按照`1`统计，很明显就可以知道有`1,2,3`这样一个顺子，但是如果按照`2`统计，其既有`1,2,3`也有`2,3,4`。

所以可以模糊感觉到，这题还带有一点贪心的意思。
即我们可以率先将牌堆中最小的牌拿出来尝试建立一个顺子。建立完后牌堆肯定会发生变化，将变化后的牌堆的最小牌继续拿出来继续建立顺子。
如此周而复始。因为顺子是连续的，所以构建牌堆时通过检查连续性就可以判断顺子的合法性，一旦不连续，直接返回False即可。

至于具体实现，要时刻找出牌堆中最小的牌，似乎可以用堆。
但是又需要实时将那些已经组成顺子的牌拿出去，似乎又要配合一个哈希表计数，同时让堆延迟删除。
既然又要延时删除，那么似乎没有用堆的必要了。我直接排序原数组，用一个指针从小到大扫描数组，
同时使用哈希表实时计数各个牌剩余数目，这样一套机制也可以做到上述算法。

具体的一些注释写在代码里了。