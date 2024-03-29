## 题目描述
给定一个字符串 s ，返回 其重新排列组合后可能构成的所有回文字符串，并去除重复的组合 。

你可以按 任意顺序 返回答案。如果 s 不能形成任何回文排列时，则返回一个空列表。

示例 1：
```
输入: s = "aabb"
输出: ["abba", "baab"]
```
示例 2：
```
输入: s = "abc"
输出: []
```

提示：
```
1 <= s.length <= 16
s 仅由小写英文字母组成
```

### 解法 哈希表 DFS回溯
做过`LC.266`之后，这题在预处理阶段就可以通过哈希表计数来判断输入字符串s能否通过重新排列来获得一个回文字符串了。

在筛掉那些必然输出空列表的输入之后，接下来就要处理那些可能被重排成回文字符串的情况。

对于这些情况，还可以进一步细分讨论。
比如我们知道，对于各类字母的计数，最多只能有一个计数值是奇数，且奇数的那个字符要放在最终回文串的中心。
于是可以分成有没有奇数两种情况讨论。

而对于构建各种回文串的过程，很显然这就是一个基于外部哈希表的DFS回溯的过程。

为了简化问题，我们可以只看回文串的前半段。
将前半段规定为一个长度为`n // 2`的列表，然后从前向后扫描各个位置，
并依次用哈希表中计数值仍然大于0的字母去填充这个位置，然后进行下一层DFS。
完了之后记得回溯复原。