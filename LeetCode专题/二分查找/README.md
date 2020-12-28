>https://leetcode-cn.com/leetbook/read/binary-search/x6q6fi/

## notation
二分查找中使用的术语：

1. 目标 Target —— 你要查找的值
2. 索引 Index —— 你要查找的当前位置
3. 左、右指示符 Left，Right —— 我们用来维持查找空间的指标
4. 中间指示符 Mid —— 我们用来应用条件来确定我们应该向左查找还是向右查找的索引

## 基本问题设定
二分查找有一个target值。这个值可能是条件中给出的，也有可能是根据题意我们自己设定的。

然后我们要从被探索的空间中寻找这个target。

被探索的空间通常是一维的数组，对于纯数字的情况，通常还会要求其是有序的。所以有时会需要将排序作为预处理步骤。

二分查找的逻辑十分简单，但是实现上有很多细节要注意。否则一不小心就会陷入无限循环之类的bug当中。

下面给出几个常用的二分查找模板。

## 模板1
```python
def binarySearch(nums, target):
    if len(nums) == 0: return -1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
```
初始条件：`left = 0, right = len(lst) - 1`
终止条件：`left > right`,注意没有等号
向左查找：`right = mid - 1`
向右查找：`left = mid + 1`

注意几点。

第一，终止条件是`left > right`没有等号，这就意味着代码中的循环条件是
`while left <= right`。这么做的好处是，当左右两个游标互相逼近的时候，势必有一天，
会相等。而相等的时候计算出来的mid必然也会是同一个值。此时根据mid值判断再将left右移或者right左移，
结果到底是返回哪个游标的值，根据题意判断就会比较清晰。

第二，两个查找条件都不停留在mid本身。这可以避免当查找空间已经缩小到两个值时，
mid落在left或者right上从而导致搜索陷入循环。

几道使用上述模板的题目：
```text
69.x的平方根
374.猜数字大小
33.搜索旋转排序数组
```

## 模板二
```python
def binarySearch(nums, target):
    if len(nums) == 0: return -1
    
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    
    # post-process
    if len(nums) != left and nums[left] == target:
        return left
    
    return -1
```
初始条件：`left = 0, right = len(lst)`
终止条件：`left == right`
向左查找：`right = mid`
向右查找：`left = mid + 1`

这个模板的关键点在于，左移操作是`right = mid`。所以，**当某个问题二分查找时，满足左移条件的同时却不能排除mid的可能，那么可以用这个模板。**

其次也要注意到，循环跳出时条件是`left == right`，所以其实最后left和right同时指向的那个元素可能未经处理（比如全程都是left在右移的情况）。
此时最后的post-process操作进行那个元素的处理。

几道使用上述模板的题目：
```text
278.第一个错误的版本
162.寻找峰值
153. 寻找旋转排序数组中的最小值
```

需要注意，其实上述几个问题，用第一种模板也可以解决。不过第二个模板每次缩小搜索区域时都不主动排除right，代码更容易看懂。

## 模板3
```python
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid
    
    # post-process
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right

    return -1
```
初始条件：`left = 0, right = len(lst) - 1`
终止条件：`left + 1 == right`
向左查找：`right = mid`
向右查找：`left = mid`


## 总结

三个模板的汇总：
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/29/template_diagram.png)

>注意，以上模板中的mid计算方式用`mid = left + (right - left) / 2`是因为C或者Java中直接left + right可能导致溢出。而这样就不会溢出。

据说绝大多数二分查找问题，都可以用模板1或者3来解决。而2是一个比较高级的做法。用于一些特定的问题比较好。

- 二分查找思路很简单，但是细节很复杂。
- 每个分支都要有处理，否则很容易造成死循环。