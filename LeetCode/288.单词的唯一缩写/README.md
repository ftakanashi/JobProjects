## 题目描述
单词的 缩写 需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。如果单词只有两个字符，那么它就是它自身的 缩写 。

以下是一些单词缩写的范例：

dog --> d1g 因为第一个字母 'd' 和最后一个字母 'g' 之间有 1 个字母
internationalization --> i18n 因为第一个字母 'i' 和最后一个字母 'n' 之间有 18 个字母
it --> it 单词只有两个字符，它就是它自身的 缩写
 

实现 ValidWordAbbr 类：
```
ValidWordAbbr(String[] dictionary) 使用单词字典 dictionary 初始化对象
boolean isUnique(string word) 如果满足下述任意一个条件，返回 true ；否则，返回 false ：
字典 dictionary 中没有任何其他单词的 缩写 与该单词 word 的 缩写 相同。
字典 dictionary 中的所有 缩写 与该单词 word 的 缩写 相同的单词都与 word 相同 。
```

示例：
```
输入
["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
[[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"], ["cake"]]
输出
[null, false, true, false, true, true]

解释
ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake", "card"]);
validWordAbbr.isUnique("dear"); // 返回 false，字典中的 "deer" 与输入 "dear" 的缩写都是 "d2r"，但这两个单词不相同
validWordAbbr.isUnique("cart"); // 返回 true，字典中不存在缩写为 "c2t" 的单词
validWordAbbr.isUnique("cane"); // 返回 false，字典中的 "cake" 与输入 "cane" 的缩写都是 "c2e"，但这两个单词不相同
validWordAbbr.isUnique("make"); // 返回 true，字典中不存在缩写为 "m2e" 的单词
validWordAbbr.isUnique("cake"); // 返回 true，因为 "cake" 已经存在于字典中，并且字典中没有其他缩写为 "c2e" 的单词
```

提示：
```
1 <= dictionary.length <= 3 * 104
1 <= dictionary[i].length <= 20
dictionary[i] 由小写英文字母组成
1 <= word <= 20
word 由小写英文字母组成
最多调用 5000 次 isUnique
```

### 解法 哈希表
并不是很难。
首先很显然需要定义一个专门用来获取单词缩写的方法。

接着，对于初始化状态的单词表，为了保存单词与缩写之间的对应关系，显然需要一个哈希表。

这里哈希表可以有两种方向选择，我们选择 缩写->单词 的方向。
这样的话涉及到一对多的情况，所以哈希表可以用`defaultdict(set)`或者`defaultdict(list)`。

最后`isUnique`中，只要简单的按照题意做判断即可。
即，输入单词的缩写是否存在于已保存的信息中；
若存在，保存信息中该缩写对应的单词是否只有一个且刚好是输入单词。