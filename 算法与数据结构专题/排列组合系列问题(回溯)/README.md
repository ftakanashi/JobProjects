# 排列组合系列问题
主要指LC中如下题目：
```text
78.子集
90.子集II

39.组合总和
40.组合总和II

46.全排列
47.全排列II
```
这些题目基本都是给出一个数组输入，然后求一些排列组合的结果。
每两道题为互相关联的一组。I和II之间的区别在于数组中是否存在重复的数字（以及能否重复使用等）。

这几道题无一例外全部都可以用回溯法的思想来做。
因为输入是一个线性数组，因此回溯法的dfs函数通常都带有参数`pos`表示从左到右扫描到的位置。
在dfs函数中，我们只处理输入数组中当前`pos`位置的数字，并且在其中开启`pos`往右的下一层DFS。
所以这类题目的大概模板是这样的：
```text
输入数组array长度为n
初始化结果容器res
（如必要）前处理，如排序输入数组等

def dfs(pos, 部分结果subres):
    if 符合收割条件：
        res.append(subres.copy())
    
    for i in range(pos, n):
        subres.add(array[i])
        dfs(i或者i+1等, subres)
        subres.remove(array[i])

        如有必要，跳过连续相同的数字
            注意，如果要跳过连续相同数字，前提条件一般是预处理时数组排序过了
            另外，为了跳过方便，通常放弃for i in range(xxx)的形式，而是采用while i < n: i += 1。
            这样只要让while i < n-1 and array[i] == array[i+1]: i+=1 就可做到填过连续相同数字，并且不越界了。

dfs(0, 空部分结果)
return res
```

下面我们一组一组来看。问题描述我就不抄了，直接讲解法。

## 子集两道题
由于求的子集没有长度要求（即使长度为零的空集也在返回的结果中），
因此dfs函数开头不需要任何条件判断，只要无脑收割结果即可。

在子集II中，因为存在重复数字，因此需要
1. 预处理阶段对数组进行排序
2. dfs函数体中，在针对`pos`位置的元素回溯后，（在这个时间点，相当于进入了没有选择`pos`位置元素的分支）跳过所有后续与`pos`位置元素相同的元素，

因此，78的代码如下：
```python
class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def dfs(pos, subres):
            res.append(subres.copy())
            for i in range(pos, n):
                subres.append(nums[i])
                dfs(i + 1, subres)
                subres.pop()
        
        dfs(0, [])
        return res
```

90的代码如下：
```python
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        n = len(nums)
        nums.sort()

        def dfs(pos, subres):
            res.append(subres.copy())
            i = pos
            while i < n:
                subres.append(nums[i])
                dfs(i + 1, subres)
                subres.pop()
                
                while i < n-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1

        dfs(0, [])
        return res
```

## 组合总和两道题
这两题如果没有上下文，直接看的话乍一眼很容易做成背包问题。
当然也能很快看出来其求的是完整的所有结果，而非一个最值，所以没法直接用背包问题做。

其实这两题其实和子集十分像，无非就是在收割结果时需要注意并不是无脑收割，而是只有符合条件`sum(subres) == target`才能收割。

显然每次在每层dfs中都`sum(subres)`会造成大量重复计算。因此可以再dfs函数中新增一个subsum参数，用来表示当前subres的总和。
这样就不需要每次dfs的时候都计算一个数组的和了。

此外，因为有目标和target作为限制，这次DFS其实可以不用每条路都走到头为止。
一个优化的办法是预处理时进行排序，而后dfs时一旦发生`subsum + nums[i] > target`的情况，则说明之后的所有数字都不用看，必然都大于`target`。

最后注意，
组合总和I中规定了每个数字可以取无限次，类似01背包和完全背包之间的差别，这里下一层dfs的入口，第一个参数将不是`i+1`而是`i`。
组合总和II则和子集II一样，因为不能有重复的答案，因此预处理排完序之后，dfs函数体中需要进行连续重复数字的跳过。
具体做法和子集II中一模一样。

这两道题代码如下：
39：
```python
class Solution:
    def combinationSum(self, nums, target):
        res = []
        n = len(nums)
        nums.sort()

        def dfs(pos, subres, subsum):
            if subsum == target:
                res.append(subres.copy())
                return

            for i in range(pos, n):
                if subsum + nums[i] > target: break
                subres.append(nums[i])
                dfs(i, subres, subsum + nums[i])
                subres.pop()
        
        dfs(0, [], 0)
        return res
```

40:
```python
class Solution:
    def combinationSum2(self, nums, target):
        res = []
        n = len(nums)
        nums.sort()

        def dfs(pos, subres, subsum):
            if subsum == target: 
                res.append(subres.copy())
                return
                
            i = pos
            while i < n:
                if subsum + nums[i] > target: break
                subres.append(nums[i])
                dfs(i + 1, subres, subsum + nums[i])
                subres.pop()

                while i < n-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
        
        dfs(0, [], 0)
        return res
```

## 全排列两道题
相比于前两组，全排列的两道题可以说稍微难一点。

大体的框架不变，还是回溯法dfs。关键问题在于，回溯到底是回溯什么东西，或者说基于什么规则进行不同全排列的构建？

一个朴素的想法是，基于插入。
换句话说，`dfs(pos, subres)`的工作是，在subres这个数组中找到一个位置，插入`array[pos]`。
显然，这个位置可以是`range(len(subres) + 1)`中的任意一个。
这么一来下一层DFS的入口就变成了`dfs(pos + 1, subres[:i] + [nums[pos], ] + subres[i:])`。

上面的做法，可以做。但是整体性能并不好。
毕竟用了切片等效率不高的操作。应该想想更好的办法。

更好的办法，就是不要基于插入，而是基于交换的做法。
具体的，我们定义`dfs(pos)`的工作为 **确定某个全排列的pos位置以及其右边放哪个元素**。
换言之，`dfs(pos)`内部，我们默认所有`pos`左边的数字排列，已经固定。

显然，我们可以保留输入的`array[pos]`位置在原地，于是下一层可以直接`dfs(pos + 1)`即可。
另一方面，这个位置也可以放任何处于`pos`右边的数字，即`for i in range(pos, n)`。
于是，只要把这些数字与当前`pos`数字互换，然后再`dfs(pos + 1)`，我们就可以得到所有情况了。

显然这两题的dfs函数，将在`pos == n-1`时进行结果收割并终止搜索。

至于II和I之间的区别，显然在扫描`for i in range(pos, n)`，并且将`pos`和`i`位置交换的过程中，
如果交换前某个`nums[i]`在前面扫描的过程中已经被交换过来一次过了，那么这次交换和之前其实是等价的，没必要再做一次。

为了标记扫描过程中，哪些数字已经交换过了，可以额外维护一个哈希集。

于是，46的代码：
```python
class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)

        def dfs(pos):
            if pos == n-1:
                res.append(nums.copy())
                return
            
            for i in range(pos, n):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]
        
        dfs(0)
        return res
```

47的代码：
```python
class Solution:
    def permuteUnique(self, nums):
        res = []
        n = len(nums)

        def dfs(pos):
            if pos == n-1:
                res.append(nums.copy())
                return
            
            seen = set()
            for i in range(pos, n):
                if nums[i] in seen: continue
                seen.add(nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]
        
        dfs(0)
        return res
```