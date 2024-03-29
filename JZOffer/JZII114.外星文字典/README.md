## 题目描述
现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。

如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。

示例 1：
```
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
```
示例 2：
```
输入：words = ["z","x"]
输出："zx"
```
示例 3：
```
输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
```

提示：
```
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成
```

### 解法 拓扑排序
这题同`LC.269`。
思路不算太复杂，就看能不能想到了。

具体来说，对于词表`words`，我们比较其中所有两两的词对。由于此表的顺序是外星语的词典序，
所以两个词比较时有一个先后顺序。

那么只要以字符单位比较这两个词，绝大多数情况下我们都可以得到某两个字母在外星语中的语序。
比如示例1中，比较`wrt`和`wrf`就知道在外星语中`t`在`f`前面，以此类推。

比较完所有词对后，我们可以得到一张有向图（但不一定连通且只有一个连通分量）。
接下来要做的，就是对这个有向图进行一次拓扑排序，只要能得到任意一个拓扑排序序列，这个序列就是答案了。

更多细节我还是写在代码注释中了。