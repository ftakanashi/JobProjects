## 题目描述
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

示例 1：
```
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```
示例 2：
```
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```

提示：
- 1 <= A.length <= 20000
- 0 <= K <= A.length
- A[i] 为 0 或 1 

### 解法 滑动窗口
首先应该明确一点，所有被修改的0在修改后应该处于同一片1的子数组中。

比如`0 1 1 1 0 1 1 1 0`，如果修改两个0为1，要是改第一个和最后一个0就很傻缺。
因为中间的0还是把两边隔开导致两边只能分开算。

在这种思想的指导下，显然这道题就变成了，找到一个最长连续子数组，最多包含K个0。
于是就用滑动窗口解。

具体算法，设置一个变量`zeros`维护窗口内0的数量。右指针向右移动，每遇到一个0，`zeros+=1`。
直到`zeros > K`。注意等于的时候还得继续扫描因为可能后面还连着一片1。

当`zeros > K`时，显然右指针指向的是0，此时将左指针收缩，直到其遇到第一个0。
此时左指针再往前一格，`zeros`回归到K。
然后右指针继续往前。

结果收割应该安排在右指针停止移动的时候。
右指针停止移动有两个地方，第一是zeros超过了K的限制，第二则是右指针来到数组末尾。

### 滑动窗口模板
因为这题是典型的滑窗题，所以这里结合这道题再写个滑窗模板。

```python
def longestOnes(A, K):
    # 初始化
    N = len(A)
    left, right = 0, 0   # 左右指针初始化,窗口就是指左右指针间的闭区间
    res = 0    # 结果变量初始化，根据题意设置
    zeros = 0    # check变量：一些用于判断窗口是否合法的辅助变量。
    # 只有合法的窗口才能继续移动右指针。check变量通常随着窗口动态变化而变化。

    # 开始滑动
    while right < N:
        zeros += (1 - A[right])    # 实时更新check变量以判断窗口是否还符合题意

        # 根据check变量，窗口不符合题意时，左指针前移
        while zeros > K:
            zeros -= (1 - A[left])    # 左指针移动过程中也别忘了动态更新check变量
            left += 1
        
        # 右指针移动过程中，每发现一个合法的窗口就记录一次结果
        res = max(res, right - left + 1)

        right += 1    # 滑动

    return res
```

利用以上模板，来应用到一道简单的滑窗题，也是这题的简单版：`LC485.最大连续1的个数`。

题目很简单，就是求出一个01数组内最大连续1的长度。直接给出套用上面模板的代码：
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        left, right, res = 0, 0, 0
        has_zero = False

        while right < N:
            if nums[right] == 0: has_zero = True
            
            if has_zero:
                while right < N and nums[right] == 0:
                    right += 1
                if right == N: break
                left = right
                has_zero = False

            res = max(res, right - left + 1)
            right += 1
        
        return res
```
初始化部分没啥可说的。
关于check变量，我这里强行设置一个has_zero来判断窗口内是否有0从而判断窗口的合法性。

进入循环后，首先是实时更新check变量。因为check变量就是一个简单的bool类型判断窗口内有没有0，因此直接看right是不是0即可。

当right指向的是0，此时窗口失去合法性。
下一步要移动左指针了。
但是注意到这么一个情况，代码跑到这个地步时，窗口一定长这样：`1 1 1 ... 1 0`。
因此其实可以将left直接移动到right。

移动到right可以吗？此时窗口仍然是非法的，含有0。
所以这里移动左指针稍微复杂一些。

首先应该继续移动右指针，直到其指向1。然后将左指针移动到右指针。
注意这里第二波移动右指针的操作也可能让右指针到达边界。如果到达边界说明之前那个窗口之后再无合法窗口，所以可以直接break。
最后别忘了左指针移动完后更新check变量。

以上代码就可以work了。

当然，这里强行为了套模板整出了个has_zero之类的check变量。实际上看了这代码也知道，没必要那么繁琐。
has_zero这个变量完全是多余的，可以去掉后调整代码。

再来用伪代码练习一次滑窗模板：
```text
初始化:
    N = len(nums)
    left, right = 0, 0 或者 0, 1
    res = 0
    check = 0

开始滑动:
while right < N:
    update(check, nums[left,right])  用最新窗口更新check
    
    while not check:    # 移动左指针
        update(check, nums[left, right])  用最新窗口更新check
        left += 1 
    
    合法时:
    res = optimize(res, right - left + 1)
    right += 1

返回结果：
return res
```

另一种表述：
```text
# 滑动窗口模板
left,right = 0, (0 or 1)
ret = total = 0
while right < len(nums):
   更新total值
   while 窗口内数据不满足要求
      1. 更新total值
      2. 收缩左边界
   更新ret最大值
返回 ret
```