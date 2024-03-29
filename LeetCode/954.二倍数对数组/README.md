## 题目描述
给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

示例 1：
```
输入：arr = [3,1,3,6]
输出：false
```
示例 2：
```
输入：arr = [2,1,2,6]
输出：false
```
示例 3：
```
输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
```

提示：
```
0 <= arr.length <= 3 * 104
arr.length 是偶数
-105 <= arr[i] <= 105
```

### 解法 哈希表 排序
这题倒不难。

题目意思虽然有些拗口，但是思考一下就可以知道，其实就是想让我们检查，数组中的数是否恰好能凑成整数对的`x, 2x`而已。

对于这样一个问题，一个很显然的思路就是排序后用哈希表统计其是否恰好能凑成。
由于可能会有负数，所以我一开始的思路是进行逆序排序，从最大的数开始扫描。
因为对于一个大数，其只能是另一个数的两倍而不用去检查他的两倍。

这样倒也可以做，但是扫描的逻辑条件会比较复杂，因为还涉及了越过零点后的反向检查（比如-2和-4，在上述逻辑中会先扫描到-2

既然要消除越过零点的影响，就想到了用绝对值来排序即可。

具体来说，我们设置一个counter，然后以绝对值为排序依据从小到大进行扫描。
扫描到数字`x`时，只需要检查`2 * x`的数量是否大于等于`x`的数量即可。
若是，则说明至少对于`x, 2x`这样的数对，是可以凑出足够多的。如果`2x`有盈余，那么需要检查`2x, 4x`对的情况。这个在后面的遍历会做。
若否，那么说明`x`本身就多余了。而又因为我们是绝对值从小到大扫描的，不可能还会有`x/2, x`对，所以可以直接返回False。
当扫描完成仍没有False，说明所有的数字都可以安排到对中。

以上逻辑还有唯一的一个漏洞，0。
比如`1, 0, 2`这组，按照上面的逻辑的代码也会返回True，因为`x==0`时，`2x`也是0。 
处理0这个特殊情况也很简单，只要在最开始检查其是否有偶数个即可。只有0是偶数个，才可能合法。