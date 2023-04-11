## 题目描述
设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 words 中的一个字符串。

例如，words = ["abc", "xyz"] 且字符流中逐个依次加入 4 个字符 'a'、'x'、'y' 和 'z' ，你所设计的算法应当可以检测到 "axyz" 的后缀 "xyz" 与 words 中的字符串 "xyz" 匹配。

按下述要求实现 StreamChecker 类：
```
StreamChecker(String[] words) ：构造函数，用字符串数组 words 初始化数据结构。
boolean query(char letter)：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 words 中的某一字符串，返回 true ；否则，返回 false。
```

示例：
```
输入：
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
输出：
[null, false, false, false, true, false, true, false, false, false, false, false, true]

解释：
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // 返回 False
streamChecker.query("b"); // 返回 False
streamChecker.query("c"); // 返回n False
streamChecker.query("d"); // 返回 True ，因为 'cd' 在 words 中
streamChecker.query("e"); // 返回 False
streamChecker.query("f"); // 返回 True ，因为 'f' 在 words 中
streamChecker.query("g"); // 返回 False
streamChecker.query("h"); // 返回 False
streamChecker.query("i"); // 返回 False
streamChecker.query("j"); // 返回 False
streamChecker.query("k"); // 返回 False
streamChecker.query("l"); // 返回 True ，因为 'kl' 在 words 中
```

提示：
```
1 <= words.length <= 2000
1 <= words[i].length <= 200
words[i] 由小写英文字母组成
letter 是一个小写英文字母
最多调用查询 4 * 104 次
```

### 解法 字典树
这道题的本意，是为了使用AC自动机这种高级算法。不过其实这道题的数据范围很小，直接用直观的字典树也可以做。
更多关于AC自动机的解释以及做法的说明，可以参考官方答案。

而用字典树做法，就直接按照题目意思一步一步分析即可。

首先，题目的主要问题就是需要随时可以快速检查某一串字符串是否能够匹配已经存在的一些单词。
当然题目里是后缀，所以单词全部都得倒序维护到字典树中。
为了方便，可将stream也倒序维护，也就是说当新来一个字母`ch`的时候，维护`stream = ch + stream`。

这样，只要检查stream是否存在于字典树中即可。
这个过程就是一个经典的字典树搜索算法。就不多说了。