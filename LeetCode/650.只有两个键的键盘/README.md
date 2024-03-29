## 题目描述
最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：

- Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
- Paste（粘贴）：粘贴 上一次 复制的字符。

给你一个数字 n ，你需要使用最少的操作次数，在记事本上输出 恰好 n 个 'A' 。返回能够打印出 n 个 'A' 的最少操作次数。

示例 1：
```
输入：3
输出：3
解释：
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。
```
示例 2：
```
输入：n = 1
输出：0
```

提示：
- 1 <= n <= 1000

### 解法1 DP
第一个想到的思路就是DP。定义`dp[i]`为`n`是`i`时需要操作的最小次数。
显然，有
```python
dp[1] = 0
dp[2] = 1
dp[3] = 3
...
```
然后观察这个序列。其实对于任意的`dp[i]`而言，要得到长度为`i`的字符串，其来源只可能是`i`某个因数`j`的基础上粘贴了`(i - j) // j`次形成。
另外别忘了复制操作也要算一次操作，所以要加上1。

综上所述，转移方程表示如下：
```python
for j in range(2. i):    # 遍历搜索所有可能的因数
  if (i - j) % j == 0:
    dp[i] = min(dp[i], dp[j] + ((i-j) // j) + 1)
```
上述转移方程还可以进行优化。
比如，无需把j真的遍历到`i-1`，因为一旦`i-j < j`，`(i-j) // j`必然是0。

另外，因为要求的是尽可能少的次数，说明`j`越大越好，所以可以以`range(i//2, 1, -1)`的形式遍历j。
且遍历过程中只要找到一个答案，就可以完成搜索直接保存答案，因为此时`j`最大，操作次数肯定最小。

由于进行两层循环，显然这个复杂度达到O(n^2)，不过好在题目规定了输入最长长度是1000，因此可以接受。

### 解法2 质因数分解
观察上面提到的`dp[i]`，可以发现这样一个现象：
对于所有质数`i`，`dp[i] == i`。

这是因为对于一个质数`i`来说，其无法通过任何1到`i`之间的中间长度的字符串获得。
反之，其只能通过将长度为1的字符串粘贴`i-1`次获得。

进一步的，对于合数`n = a*b`（其中ab都是其质因数），其实就说明了这样一个事：
要得到`n`长度的字符串，可以是`a`长度的字符串复制1次+粘贴`b-1`次获得。
整理一下，一般化，可知，要知道输入是`n`时的答案，只要求出其所有质因数，然后把这些质因数求和即可。

例如`n=1000`时，`1000 = 2*2*2*5*5*5`，所以答案就是`2+2+2+5+5+5 = 21`。