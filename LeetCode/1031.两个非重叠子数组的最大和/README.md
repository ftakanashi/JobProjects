## 题目描述
给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。

长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。

子数组是数组的一个 连续 部分。

示例 1：
```
输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
```
示例 2：
```
输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
```
示例 3：
```
输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
```

提示：
```
1 <= firstLen, secondLen <= 1000
2 <= firstLen + secondLen <= 1000
firstLen + secondLen <= nums.length <= 1000
0 <= nums[i] <= 1000
```

### 解法 滑动窗口 模拟
这题的做法还是挺有意思的，看上去是一个"滑动窗口的滑动窗口"，但是内核上来说还是一个DP。感觉上则更像是一个简单模拟。

首先，子数组1和子数组2的前后没有规定，但是长度有区别说明这两个数组不是完全对等的。
但是另一方面，我们可以先假设子数组1在左边，做一个helper函数求出答案，之后只要兑换helper的两个长度参数即可。

设两个数组的长度分别为`l1`和`l2`，即参数中的`firstLen`和`secondLen`，起始下标分别为`i`和`j`。
显然初始情况下，两个数组分别是`nums[:i]`和`nums[i:j]`。
此时两个数组各有一个当前的和`s1`和`s2`。

然后开始向右滑动。
首先滑动数组2，变成`nums[i+1:j+1]`并且得到一个新的和`s2'`。显然，`s2'`是`s2`加上了`nums[j] - nums[i]`。
同理，滑动数组1可以类似地得到`s1'`。
以此类推。

最关键的来了，在整个滑动过程中，我们维护所有出现过的`s1`的最大值，也就是说每滑动一步都维护一个`s1_max = max(s1_max, s1')`。
在这个时间点并且往后地所有时间点上，子数组2与当前的`s1_max`对应的子数组1之间是没有重叠的（因为遍历时从左到右进行的）
因此此时可以直接更新答案`ans = max(ans, s1_max + s2')`。

如此，当滑动到最后，一定可以找到全局的两个子数组和的最大值。
当然别忘了此时的一个大前提是子数组1一定在左边。接下来将两个长度互换之后就可以求子数组2一定在左边时的全局最大值。
取两个值中较大者即可。