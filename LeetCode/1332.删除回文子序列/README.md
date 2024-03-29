## 题目描述
给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 子序列。

返回删除给定字符串中所有字符（字符串为空）的最小删除次数。

「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。

「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。

示例 1：
```
输入：s = "ababa"
输出：1
解释：字符串本身就是回文序列，只需要删除一次。
```
示例 2：
```
输入：s = "abb"
输出：2
解释："abb" -> "bb" -> "". 
先删除回文子序列 "a"，然后再删除 "bb"。
```
示例 3：
```
输入：s = "baabb"
输出：2
解释："baabb" -> "b" -> "". 
先删除回文子序列 "baab"，然后再删除 "b"。
```

提示：
```
1 <= s.length <= 1000
s 仅包含字母 'a'  和 'b'
```

### 解法 直接判断
…这题是很久每遇到过的"你特么在逗我"型的题目了。

首先注意审题，字符串只有a和b两种字符，并且删除的是子序列而不是子串。

刚开始我考虑了能不能通过模拟删除的做法或者其他什么思路做，但是没有很しっくり来る的办法。

一看答案，傻眼了。

对于符合题目输入要求的任意一个字符串，首先如果这串本身是回文串，那么毫无疑问答案是1。
若不是，由于题目是删除子序列，我可以直接一口气删除所有a或者所有b，而所有字符相同的一个序列必然是一个回文序列…
因此，若串本身不是回文串，直接返回2即可。

只能说示例3是一个陷阱，虽然输出答案也是2，但是解释里的删除方法还是一般的删除回文序列的方法，因此思考误入歧途了。