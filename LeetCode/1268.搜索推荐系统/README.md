## 题目描述
给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。

示例 1：
```
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
```
示例 2：
```
输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```
示例 3：
```
输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
```
示例 4：
```
输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]
```

提示：
```
1 <= products.length <= 1000
1 <= Σ products[i].length <= 2 * 10^4
products[i] 中所有的字符都是小写英文字母。
1 <= searchWord.length <= 1000
searchWord 中所有字符都是小写英文字母。
```

### 解法 字典树 有序列表
提供一种比较直观的思路。
显然，基于products列表中的每个单词，我们可以构建一颗字典树。
然后只需要依次扫描searchWord的各个前缀，搜索字典树，并且将找到的前三个结果返回即可。

以上思路虽然也可以过，但是耗时很长，因为每个query的前缀都要从头开始扫描字典树。
下面则是一个稍微优化的思路。

以上我们使用的经典的字典树结构，实际上我们可以稍作修改。
在一个字典树节点中，我们使用`sortedcontainers.SortedList`保存这个子树中所有被保存的单词。
并且由于是有序列表，所以直接取前三个就能返回。

此外还有一个小的优化点，就是在遍历前缀的时候，如果某个前缀搜索出为空结果，那么实际上就可以马上退出，
因为之后的所有搜索一定都是空结果。此时可以跳出搜索程序，直接让ans到`len(searchWord)`为止，打满空列表即可。