## 题目描述
累加数 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。

给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

说明：累加序列里的数 不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

示例 1：
```
输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
```
示例 2：
```
输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
```

提示：
```
1 <= num.length <= 35
num 仅由数字（0 - 9）组成
```
```
进阶：你计划如何处理由过大的整数输入导致的溢出?
```

### 解法 暴力扫描
初看此题，第一个想到的办法是暴力DFS。
但是思索了一会儿之后发现可能并不用那么复杂。

我想到的DFS思路是，dfs函数接收扫描开始位置以及扫描到此处的前两个数作为依据，
先计算出第三个数然后从当前位置扫描看是否match，若match则更新前两个数，并且将扫描位置向后移动相应格子。

但是从更加宏观的角度看，对于题目中提到的这样一个斐波那契数列，只要确定了前两个数字，整个数列其实就确定了。
换言之，我们只需要设置两个指针分别指向第一个和第二个数的末尾，接下来要做的，就是扫描一遍剩余数列，看是否符合斐波那契规律即可。

显然这样一个做法是O(n^3)的。

给出了代码，不过代码中还有许多可以优化的点，时间有限这里就不说了。
更多详细解释写在了注释里。