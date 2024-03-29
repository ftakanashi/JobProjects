## 题目描述
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。

生成的测试用例保证结果符合 32-bit 整数范围。

示例 1：
```
输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]
```
示例 2：
```
输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7
```

提示：
```
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= left <= right <= 109
```

### 解法 遍历求解
一个数组会有很多很多子数组。但是显然，所有带有大于right的值的子数组都不符合要求。
换言之，首先我们可以找出那些大于right的值的位置，这些位置就是分割点。

若无对left的要求，那么这题就是分割后再统计每个分片的长度，然后计算子数组个数最后加和起来就行了。

但若引入了left的要求，显然我们还需要排除那些只含有小于left值的数组。这些也是分割点。
但是这个比较麻烦的在于，一个小于left的数，只要其周围有在left和right间的数，那么包括它也是没关系的。

想了一会儿没想到什么好办法。加上今天还要转正答辩…就直接看答案了。

答案的核心在于，构建一个`check(upper)`函数。
这个函数的功能是：
找出nums数组中，所有最大值小于等于upper的子数组的个数。而最终答案，是`check(right) - check(left - 1)`。
大呼内行啊。

至于这个check函数，实现起来也不复杂。
对于长度为`x`的数组，要统计其子数组个数，当然可以用高斯公式算：`x * (x + 1) / 2`。
但是这个数字本身也可以通过不断累加得到。即：
```python
res = cur = 0
for num in nums:
    cur += 1
    res += cur
```

而在check函数中，我们只需要加上一个简单的`num`是否小于等于`upper`的判断即可。若否，则直接将`cur`置零即可。

总的check函数：
```python
nums = [2,9,2,5,6]
def check(upper):
    res = cur = 0
    for num in nums:
        if num <= upper:
            cur += 1
        else:
            cur = 0
        res += cur
    return res
```

说实话今天这题虽然整体不难，但是总感觉这个解法真的有点妙啊。