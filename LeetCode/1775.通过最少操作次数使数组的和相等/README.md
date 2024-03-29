## 题目描述
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。

示例 1：
```
输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
```
示例 2：
```
输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
```
示例 3：
```
输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。
```

提示：
```
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
```

### 解法 贪心
读完题后应该意识到，两边的数组各自修改都是比较独立的操作，不会互相影响。
因此就应该抓住关键，要让两边和相等，最主要关注的就是每个数组中的各个数字的个数，以及这些数字的和。

而要让两边的和最快地相等，显然应该尽量把和小的数组中的1替换为6，较大的数组中的6替换为1（当然有可能不存在1或者6，总原则就是尽量选小的/大的数字替换）

于是首先有一个很显然的结论，就是当较小数组的所有数字都替换成6后，依然没有较大数组所有数字替换为1后的和大，此时直接返回-1。

对于剩余情况，如果比较机械地一个个判断，会比较麻烦。
这里，我们抓住差值这个重点。计算两个数组和最初的差值，然后计算两个数组中每个数字的"贡献值"。
比如较大数组中的6和较小数组中的1，贡献值都是5，以此类推。

这样，我们只要统计出所有贡献值和相应的计数值，然后从大到小地尝试减去各个贡献值，直到差值小于等于零即可。

描述可能还是有点模糊，建议直接看代码。