## 题目描述
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

示例 1：
```
输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
```
示例 2：
```
输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
```
示例 3：
```
输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
```

提示：
```
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
在 words[i] 和 order 中的所有字符都是英文小写字母。
```

### 解法 自定义排序
题目不复杂。

很显然要根据order给出的新的字母排序，来判断words中的顺序。
因为字典序没有什么特别直接判断的办法，所以我采用了将所有单词都转化成字母序号的元组的形式来比较。

即先构建一个字母到序号的映射哈希表：`order_dict = {ch: i for i, ch in enumerate(order)}`
接着将所有字母都进行转化：`tuple(order_dict[ch] for ch in word)`

如此，只需要比较这些元组之间的大小关系，就知道字典序了。