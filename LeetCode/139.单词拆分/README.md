## 题目描述
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。你可以假设字典中没有重复的单词。

示例 1：
```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```
示例 2：
```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
```
示例 3：
```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

### 审题
这道题其实是一道比较经典的，既可以用探索（DFS），也可以用DP来做的题。

而很多题目都是这道题的变体，所以掌握这道题的套路很有好处。

### 解法1 记忆化DFS
没啥可说的。dfs函数的参数可以设置为剩余为探索部分的起始下标start。

显然，递归终止条件是`start == len(s)`。

而在当前未探索区域的开头找到一个wordDict中的单词，准备进行下一层DFS时需要注意，下一层DFS的起始坐标是`end + 1`。

### 解法2 DP
dp数组定义如下：
设置长度为`len(s) + 1`的dp数组。`dp[i]`表示字符串`s[:i]`能否被要求的wordDict恰好分割，因此其保存的dp值是布尔量。

针对某个位置`i`，遍历其所有前面的位置`j`，状态转移方程是：
```python
if dp[j] and s[j:i] in word_set: dp[i] = True
else: dp[i] = False
```
注意if条件中`i,j`都是比实际下标大1的，因为`dp[0]`表示空串能否被分割，这里默认其是True。
而`s[j:i]`才是我们要考察的子串。

显然这个过程是O(n^2)了。

一个可能的优化思路：事先先找到wordDict中的最长的单词，这样j可以不用从0开始，而从`i - max_len`开始即可。