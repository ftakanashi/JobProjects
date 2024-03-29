## 题目描述
给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。

示例 1：
```
输入：n = 12
输出：true
解释：12 = 31 + 32
```
示例 2：
```
输入：n = 91
输出：true
解释：91 = 30 + 32 + 34
```
示例 3：
```
输入：n = 21
输出：false
```

提示：
```
1 <= n <= 107
```

### 解法 三进制
这题挺有意思的。乍一看似乎要通过回溯或者DFS之类的办法暴力搜索。
但是实际上暗藏玄机。

把一个数字表示成某个数的幂的和，实际上就是在判断这个数字能否表示成该数字的进制的特定形式。

这里，特定形式就是指进制转换之后所有位数的数字不是1就是0。

二进制下，因为本来所有数字就都是0或者1，所以所有自然数都可以被表示成2的幂的和。
对于三进制也就是这道题的场景，就不是如此了。
比如`9 = 100(3)`，`10 = 101(3)`，`11 = 102(3)`，`12 = 110(3)`。可以看到，11就不能被表示成3的幂的和，因为有一个2存在。

到这里，这题就很简单了，先尝试将目标数字转化为三进制，然后判断三进制各个位数是否有2即可。