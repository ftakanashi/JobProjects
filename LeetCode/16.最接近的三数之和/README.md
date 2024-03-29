## 题目描述
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

示例 1：
```
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```
示例 2：
```
输入：nums = [0,0,0], target = 1
输出：0
```

提示：
```
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
```

### 解法 双指针
题目的答题框架和上一题 `LC.15` 是一样的，
也是先排序整个数组。然后固定一个小值后在右边区域内头尾双指针向中间逼近，以找到三数和最接近target的情况。

另外这题保证只有一个答案，且只要返回和而不需要具体的数字组合，反倒是比上一题更加方便了。
直接按照上面的思路描述做就完了，不用考虑很多东西。

具体的，排序整个数组后，从左到右固定一个`pivot`值。
然后寻找`pivot + 1, n - 1`这个区间内的值`i, j`，使得 `nums[pivot] + nums[i] + nums[j]` 尽可能接近 `target`。

当然如果某次尝试出来的值直接等于了`target`，那不可能有更接近的值了，直接返回就完了。