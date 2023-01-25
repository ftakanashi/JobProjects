## 题目描述
给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。

给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

示例 1：
```
输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。
```
示例 2：
```
输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
```
示例 3：
```
输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。
```

提示：
```
1 <= sequence.length <= 100
1 <= word.length <= 100
sequence 和 word 都只包含小写英文字母。
```

### 解法 模拟
这题看起来不难，但是实际做一下好像还是有点复杂的……

基本框架就是暴力，但是怎么合理地暴力，也还是有门路的。最最暴力的办法， 答案最多只能是`len(sequence) // len(word)`。
所以我就检查`word * 1`开始到`word * k`为止是否存在于`sequence`中就完事了。
这样的做法也能AC，就是效率差了一些。

这里可以引入一点DP的思想。设长度为`n = len(sequence)`的DP数组，其中`dp[i]`表示下标`i`处为结尾的子字符串其含有的连续重复word的最大数量。

显然，当`sequence[i-m+1:i+1] == word`时, `dp[i] = dp[i-m] + 1`（注意`i`刚好是`m-1`的时候下标会越界，要注意特殊处理），否则就是`0`。
按照这个规则写DP即可。

前半个条件可以方便地使用`endswith`方法搞定，也可以自己挨个字符遍历，这样的话会稍微麻烦一点但是更加底层咯。