## 题目描述
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。

例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

示例 1：
```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```
示例 2：
```
输入：nums = [0,1,0,3,2,3]
输出：4
```
示例 3：
```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

提示：
- 1 <= nums.length <= 2500
- -104 <= nums[i] <= 104
 

进阶：
- 你可以设计时间复杂度为 O(n2) 的解决方案吗？
- 你能将算法的时间复杂度降低到 O(n log(n)) 吗?

### 解法1 DP
这也是一道比较经典的DP题。

经典在于，打破对于DP的一些固有认识。
以往说到对一维数组DP，那就是初始化一个数组后，线性地从左到右扫描过去依次更新dp数组，然后最终取出dp数组中的某个值作为输出。

但是这里，要意识到，对于dp数组的更新过程不一定是一个线性的操作。

定义dp数组为以每个位置为末尾的子序列中，最长的递增子序列的长度。
比如`0 4 1 2 3 5`这个例子。
最开始`dp[0]`显然是1。
`dp[1]`也不难求，由于`nums[1] > nums[0]`，所以`dp[1] = dp[0] + 1`。
`dp[2]`就不太对劲了，因为如果将其加入子序列，必须得知道子序列前一个数字是啥。
然而这个数字可能是0，也可能是4。

因此，此时就需要对所有小于当前位置的位置遍历，并寻找其中所有可能小于当前位置值的数字，然后求解dp，取其中最大值。

换言之，这是一个O(n^2)的过程。

dp数组更新完成后，直接去其中最大值即可。

### 解法2 贪心+二分查找优化（单调栈变体）
对于上述DP过程，一个缺点是，对于位置`i`，要线性扫描所有`0 <= j < i`的`j`。

如果这部分可以做到有序，那么就可以用二分查找来花O(logn)的时间找到对应值。

事实上我现在还知其然但不知所以然。下面只是单纯把这个算法给描述一下，脑补一下之后也知道其确实有效。

但是不知道该如何解释…

算法：
维护一个单调数组（或者你也可以称之为单调栈）`d`。现在从左到右扫描`nums`，对于扫描到的数字`nums[i]`如果大于栈顶，那么直接入栈，
如果小于栈顶，那么通过二分查找找到`d`中第一个比`nums[i]`小的数，其位置为`k`，然后更新`d[k+1]`为`nums[i]`。

写几个例子脑补一下可以发现上述算法是有效的。
但就是，`d`的意义不太理解。他维护的不是最终得到的那个最长子序列，但是其长度确实一定是最长递增子序列的长度。

有的答案说，`d[k]`维护的，是某个递增子序列长度为`k+1`时末尾数的值，但是也不是太严谨，因为长度为`k+1`的递增子序列不止一个啊…

总之先把答案抄上了。

#### 2021/07/25 追加笔记 关于解法2的解释
对于解法2，最大的疑惑还是在于，这种做法不是经典的单调栈套路。即当碰到新来数字比栈顶小的情况时，不是将栈进行pop直至符合条件，而是采取了在栈中
搜索比新数字小的最大数字，并且修改其后一个位置的数字。

这里的疑惑无非是两点，第一，为什么不能pop栈；第二，为什么要替换数字。

第一点，如果pop栈了，显然在很多情况下都无法得到最大值。比如`2 3 4 5 100 1 101`这个例子。一旦扫描到了1，如果进行pop栈，那就失去了将之前积累
的单调栈长度继续在1之后续长度的可能。因此无法得到最大的递增子序列。

第二点，不pop栈我知道了，那么为什么还要去替换数字呢？能不能不替换数字？
从结论来说，当然不能不替换数字。比如示例中的`10 9 2 5 3 7 101 18`这个例子。如果不替换数字，那么显然在10入栈后，后面的9，2，3等数字都无法入栈。
换言之，这个栈维护的最长递增子序列，永远是10开头的，失去了检查那些以后面数字开头的子序列的机会。
然而我们知道这个例子的答案是2 3 7 101，所以不替换数字也无法获得正确答案。

关于这种套路，更难一点的题目可以参考`LC.1713`