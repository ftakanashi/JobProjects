单串属于线性DP中最简单的一类问题。

根据问题具体情况不同，单串问题在计算dp值`dp[i]`的时候，大概可以分为两类。

第一，每个i必须取的类型。
第二，针对一个特定位置i，可取可不取。

单串问题的通用状态转移方程如下：
```text
dp[i] = f(dp[i-1], dp[i-2], ..., dp[0])
```

根据转移方程的函数f的不同，又可以被细分为
`dp[i]`依赖于O(1)个子问题答案的类型 以及
`dp[i]`依赖于O(n)个子问题答案的类型

### LIS问题系列
典型的单串DP问题系列。

属于每个i必取，并且依赖O(n)个子问题答案的类别。

例题
```text
最长上升子序列
最长递增子序列个数
俄罗斯套娃信封问题 - LIS
```

针对LIS问题，如果只是求最长的递增子序列长度，不采用DP策略也可以做。
DP的时候因为要依赖于O(n)个子问题答案，所以最终需要两层循环即O(n^2)复杂度。

而如果使用贪心+二分查找的办法（也可以称为非典型单调栈），则可以在O(nlogn)的复杂度下得到结果。
这个算法解LIS代码如下：
```python
from bisect import bisect_left
def lis(nums):
    stack = []
    for i in range(len(nums)):
        idx = bisect_left(stack, nums[i])
        if idx == len(stack):
            stack.append(nums[i])
        else:
            stack[idx] = nums[i]
    return len(stack)
```