## 题目描述
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
```
输入: nums = [1,2,3,1], k = 3
输出: true
```
示例 2:
```
输入: nums = [1,0,1,1], k = 1
输出: true
```
示例 3:
```
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
```

### 解法 哈希+滑窗
下标绝对值的差最多是k，这也就是说需要在一个长度为k+1的滑窗里寻找相应的下标才行。

于是思路就出现了。
滑窗滑动过程中维护一个哈希集用于保存窗口中出现了的数字。

当滑动窗口，先将左边界数字remove，然后尝试add新进来的数字。
显然，如果新进来的这个数字如果已经存在于集合中，那么就可以直接返回True。

滑动窗口滑完仍然未返回，则返回False。

注意滑窗建立前，数组的前k+1个元素需要提前额外处理。此外也要注意，k大于`len(nums)`的情况。（代码中采取了分片的办法所以没有额外讨论）。