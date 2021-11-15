## 题目描述
实现一个 MapSum 类，支持两个方法，insert 和 sum：
- MapSum() 初始化 MapSum 对象
- void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
- int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

示例：
```
输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
```

提示：
```
1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum
```

### 解法 哈希表
一句话概括一下题意，就是实现一个可以进行字符串前缀统计的哈希表呗。
说到字符串前缀的统计和处理，第一时间肯定就想到了用Trie字典树。

因为要求所有符合要求前缀词的值的和，肯定就需要在Trie节点中添加一个value属性。
这样每个单词进来后长树的时候每个节点都加上相应的新值就可以了。
同时因为字典树自带exists功能，所以基础哈希表功能也有了。

但是从更加直接的思路想，我甚至觉得不需要字典树。直接两个哈希表就可以了。
第一个哈希表是基础哈希表，记录所有键值对。第二个哈希表是前缀哈希表，记录所有出现过的前缀以及该前缀对应的值的和。
而且对比第二个哈希表和Trie树，其实空间复杂度是类似的。但是时间复杂度上，哈希表可以O(1)就查询到值，所以更优。
当然第一个哈希表就是属于无法避免的一个额外空间。属于空间换时间了。

具体的分析就不说了。代码也很简单。