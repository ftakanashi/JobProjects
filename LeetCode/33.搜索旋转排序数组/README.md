##题目描述

给你一个整数数组 nums ，和一个整数 target 。

该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

 
示例 1：
>输入：nums = [4,5,6,7,0,1,2], target = 0
>
>输出：4

示例 2：
>输入：nums = [4,5,6,7,0,1,2], target = 3
>
>输出：-1

示例 3：
>输入：nums = [1], target = 0
>
>输出：-1
 

提示：
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- nums 中的每个值都 独一无二
- nums 肯定会在某个点上旋转
- -10^4 <= target <= 10^4

### 解法1 二分搜索
如果是一个没有旋转过的数组，显然一般二分搜索就可以解决了。

由于是旋转过的数组，相当于这个数组以某个位置为界。前面是一个有序数组，后面也是一个有序数组。

因此一个思路就是，先找到这个边界`turn`，然后看target是否在`nums[0:turn]`还是`nums[turn+1:]`中。

如果target可能在某个范围内，那么就再进行一次二分搜索。

由于找turn point的二分搜索和在范围内找target的二分搜索是顺序上互相独立的。所以整体复杂度还是二分搜索的O(logn)。

上述方法整体代码过于复杂，有一些匪夷所思的特殊case要处理。下面给出一个优化版本

### 解法2 优化的二分搜索
找turn point是为了找到两个有序的子数组。
但是实际上在二分查找turn point的过程中出现了可以确定的有序子数组。

所以，每当发现可以确定是有序的一个区间的时候，就可以判断target是否可能存在于这个区间中。如果可能直接搜索就完事儿了。

