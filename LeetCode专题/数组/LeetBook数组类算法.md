>https://leetcode-cn.com/leetbook/detail/all-about-array/

# 做好初始定义
根据题意在数组中划出一部分"始终合法"的序列，然后扫描整个数组的过程中不断地扩张这部分。

扩张具体做法可以是直接覆盖也可以和后续元素的交换。

具体的代码来说，由于需要一个游标i用来维护合法序列的边界，另一个游标j用来扫描整个数组，因此至少需要两个指针。

## 例 283.移动零
定义数组的`nums[0:i+1]`部分始终是非零序列。

那么在扫描过程中，碰到不是0的就覆盖到这个序列的末尾，不断扩张这个序列。
当扫描完成时，这个序列之外的其他部分直接赋值为0即可。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        while i < len(nums):
            nums[i] = 0
            i += 1
```

## 例 27.移除元素
其实是上例的一般化场景。
定义数组的`nums[0:i+1]`部分始终是非指定val值序列即可。

由于是移除，所以扫描完成后，i之后的序列都可以不用管。

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
```

## 例 26.删除排序数组中的重复项
定义`nums[0:i+1]`是无重复项的序列。

由于题目给出的是排序数组，所以判断一个数字是否已经存在于无重复项序列中只要看他是不是等于当前序列边界值即可。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
```

注意，这题和上面不同。外部没有给出val或者0之类的值用于比较，用于比较的是`nums[i]`本身。
话说回来，其实上面两题的合法序列不是`nums[0:i+1]`，而是`nums[0:i]`。

而这题，由于要对比合法序列最末尾值，所以才是`nums[0:i+1]`。同时，也是因为这一点，
交换/赋值操作应该放在`i += 1`后面。

## 例 80.删除排序数组中的重复项II
定义`nums[0:i+1]`是元素最多只出现两次的序列。

比上题稍微复杂一点。显然需要维护一个count用来记录当前合法序列的末尾值，在合法序列中出现了几次。

当出现次数等于2次时，就不能扩张合法序列。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        count = 1
        while j < len(nums):
            if count < 2 or nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                if nums[j] != nums[i - 1]:    # 注意：i已经+=1了
                    count = 1
                else:
                    count += 1
            j += 1

        return i + 1
```

上面代码需要注意两个点。

第一，注释里也写了，我要比较的当两个值不等所以进入分支时，重置count为1的操作。
条件中的`nums[i - 1]`，因为此前`i`已经`+=1`。

第二，重置count为1还是count加1的操作不能反了。即，`count < 2 or nums[j] != nums[i]`这个操作，
其实隐含着同时`count < 2`并且`nums[j] != nums[i]`的情况。
此时，显然是要优先重置count为1而不是加1。

## 例 75.颜色分类
最简单的办法，就是把整个数组排个序就行了。

至于常数空间，一趟扫描的算法：
可以沿用上述例题的思路。只不过这次，是指定两个指针L和R。
分别定义`nums[0:L+1]`全是0，定义`nums[R:len(nums)]`全是2，剩余部分全是1即可。

这么一来第一版代码就很好写出来了。即，浮动游标扫描，碰到0则通过交换扩张L，碰到2则通过交换扩张R。
不过显然出现了一个问题，当交换过来的值不是1的时候，i不能继续往前扫描而是要待在当前位置继续工作。

这么一来，可能可以写出代码类似如下：
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l = -1
        r = len(nums)

        while i < r:

            if nums[i] == 0:
                l += 1
                nums[i], nums[l] = nums[l], nums[i]
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
```      
但是一跑，发现了问题。脑补上面思路的时候，默认了i总是在l的右边。但是如果i和l是相同位置，
比如输入第一个就是0的时候，显然第一步，l也变成了0。之后再循环，i还是在第一个位置不变，反倒是l往右移动。
这显然是不符合预期的。

为了解决这个问题，可以强行让i始终不和l相等，换句话说，如果l和i相等了，则意味着`nums[i]`是0肯定没错，
因此可以直接`i+=1`让i继续往后扫描。

具体来说，在`nums[i] == 0`的分支里加上一个判断即可。
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        l = -1
        r = len(nums)

        while i < r:

            if nums[i] == 0:
                l += 1
                if l == i:
                    i += 1
                else:
                    nums[i], nums[l] = nums[l], nums[i]
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
```

当然这些都是细枝末节的事儿，主要思想是，维护两个"合法序列"，分别一头一尾。

# 利用基础算法思想

## 例 75.颜色分类
有点强行的意思。

因为值只有0，1，2三种，所以可以采取基数排序的想法。
换言之，扫描一遍数组把所有数字归类进三种桶，然后再按顺序遍历各个桶把原数组复现出来即可。

代码比较简单就不写了。

## 例 215.数组中的第K个最大元素
乍一眼直接排序然后输出就可以了。

不过其实仔细想想，不用排序到最后。如果用的快速排序，可以想到，其实只要看某次递归时，
pivot左右区间长度即可。

如果右区间刚好等于`k-1`的话，那么pivot本身正好是要找的数字。

如果右区间小于`k-1`且长度为r的话，那么就在左区间中继续寻找左区间中第`k-r-1`大的数字。

如果右区间大于`k-1`，那么就在右区间中找第k大的数字。

## 例 88.合并两个有序数组
都不用乍一眼…就知道是归并排序的merge部分啊。

*当然如果用了归并排序的merge，是需要额外的空间的。如果不用额外的空间，那么考虑使用三指针就可以了。
i,j分别指向两个数组有效部分的末尾，k指向nums1的真的末尾。*

# 双指针对撞
所谓双指针对撞，就是设置两个指针
```python
i, j = 0, len(lst) - 1
```
一个从前往后，另一个从后往前依次扫描。具体什么情况下哪个指针走，走几步之类的还是看具体题意。

## 例 167. 两数之和II - 输入有序数组
不解释…

## 例 125.验证回文串
不解释…这题稍微麻烦一点的在于，他不管大小写和非字母数字字符。
判断的时候把这些去除就行了。

## 例 345.反转字符串中的元音字母
不解释

这题注意区分大小写，所以valid字符是`"aeiouAEIOU"`

## 例 11.盛最多水的容器
这题还是要解释一下。

前面各个题，如果想到了用前后双指针对撞的办法，那么很简单。
这是因为所谓的"什么情况下哪个指针走几步"的问题十分清晰明了。

比如上题中，只要字母不是元音字母就往前走。当两个都是元音字母时就swap然后两个指针再各自前行一步。

但是这题稍微有点难度的地方就在于，没有那么直截了当的条件了。此时就要我们自己思考一下条件。

可以看出，决定装得下多少水的主要因素是两个指针间距`j - i`以及两块板中较短的那块`min(height[i], height[j])`。

不妨假设左边的`height[i]`比较小，此时右边的指针就算往里移动，水量只会减少。一来水平面不会变高只会变低，
二来间距还变小了。因此，为了探索可能的更大的水容量，只能让height更小的左指针往里面走。

如果稍微再想得深一点，当`height[i] == height[j]`的时候，该怎么办呢。其实这时候，无论谁移动水容量都会变小，所以其实无所谓谁都行。

至此得到一个模糊的，没有经过严谨证明的结论，就是谁小谁往里面走。

编程而言，至此就够了。

如果还想要稍微优化一下。那么可以考虑，每次走的时候记录初始值，那些小于初始值的height可以直接跳过，因为其不可能和一个原本大于初始值的更高的
板子围出更多的水。

代码如下
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_volumn = (min(height[i], height[j]) * (j - i))
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            max_volumn = max((min(height[i], height[j]) * (j - i)), max_volumn)
        
        return max_volumn
```

# 双指针技巧 - 滑动窗口
滑动窗口也是定义两个指针。只不过这两个指针不是往里走，而是往一个方向走，形成一个
随着扫描长度不断变化的窗口。

程序要随着变化的窗口不断判断其是否符合一些条件，然后进行指针的移动。
还是那个问题，在什么情况下，移动左指针，什么情况下移动右指针。

同时，注意始终保持窗口的长度是正值，即`i <= j`。

看到一些求数组的连续子数组，字符串的子串等问题，基本都可以用滑动窗口

## 例 209.长度最小的子数组
首先还是说要注意仔细审题。我一开始以为窗口的值必须刚好等于target，结果写完之后才发现
只要大于等于即可。。

显然，滑动窗口从左向右移动时，当窗口中数字总和不到target值时，只能不断扩展右边界加大总和。

某一天，总和大于等于了target，此时显然记录长度并收缩左边界。

这题中由于最小长度只能是1，所以维持窗口长度是正值并没有很大意义。因为一旦`i == j`并且还收缩左边界，那么此时肯定是这单个数就已经大于等于target
值了，所以最小长度1被记录。那么管你后面是什么内容，程序出错成什么样，最终都会返回1。

下面代码中姑且对窗口长度为正值做了控制，但其实拿掉`i <= j`这个条件也没事。
```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = j = 0
        min_len = float('inf')
        while j < len(nums):
            total = sum(nums[i : j+1])
            if total >= s and i <= j:
                min_len = min(min_len, j - i + 1)
                i += 1
            else:
                j += 1
        
        return 0 if min_len == float('inf') else min_len
```

### 优化
上面对窗口内数字求和进行了列表的切片。切片会额外需要一些内存，所以如果能避免切片就好了。

注意滑动窗口类型问题中，由于窗口是连续变化的，像窗口的和这种性质也会是连续变化的。
因此total可以不要一次次独立地去求，而是每次缩进左边界之前减去相应数字，每次扩展右边界之后加上相应数字，
这样只要维护一个int类型的变量就可以知道实时的滑动窗口内数字总和了。

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = j = 0
        min_len = float('inf')
        total = nums[0] if len(nums) > 0 else 0
        while j < len(nums):
            if total >= s and i <= j:
                min_len = min(min_len, j - i + 1)
                total -= nums[i]
                i += 1
            else:
                j += 1
                total += nums[j] if j < len(nums) else 0 
        
        return 0 if min_len == float('inf') else min_len
```
注意一些边界情况。比如nums为空。
再比如`j += 1`之后如果已经结束，那么此时total再加`nums[j]`就越界了。