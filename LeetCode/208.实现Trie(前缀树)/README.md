## 题目描述
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
```
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
```

示例：
```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

提示：
```
1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
```

### 解法 经典实现方式

#### 什么是Trie
来了一个全新的数据结构。前缀树，或者也叫字典树。

前缀树本质上是一个有根的多叉树。至于每个节点能有几个分叉指向子节点，与所谓的字典空间有关系。
比如这道题规定了所有相关的字符串都是小写字母，因此这里的每个节点都有26个分叉指向子节点。

前缀树顾名思义，常用于前缀的判断。
以字符串场景为例，通常在维护一定数量的字符串到树中之后，针对这个前缀树，我们可以给出一个新的字符串Q。
我们可以查询，这个Q是否是之前那批字符串中的一个或者某一些的共同的前缀。

#### 实现
联想二叉树，其实只要实现一个节点类，因为节点之间用指针联络，因此给出根节点也就相当于给出了整棵树。

Trie也同理。只不过这里题目给出的框架是把那些接口方法也都放在了节点类`Trie`中了。
其实完全可以实现一个`TrieNode`节点模仿二叉树的节点类`TreeNode`，然后在`Trie`类中指定根节点`self.root`再用工具方法处理。
这里就不赘述了。

按题目意思，前缀树需要实现的方法包括`insert`，`search`和`startsWith`。
`insert`就是充入字符串的方法，没什么可说的。
`search`和`startsWith`差不多，区别是前者是搜索一个整个单词在不在树中，而后者是搜索某个前缀在不在树中。
为了判断扫描到某个节点时是否恰好是某个单词的结尾，还需要在节点类中安排一个`end`的布尔值。
>注意，某个节点是不是end与其是不是叶子节点并不等价。叶子节点的end必须是True。
>但当树进一步生长，叶子节点变成内部节点之后，其end仍然保持True。
>
>比如将app和apple充入树中。此后search app，仍应该返回True，所以处于内部节点的第二个p的end仍然是True。

另外一般都用数组来维护子节点指针，但是Python的话可能用字典更方便（就像并查集的实现那样），因此我用了字典实现。

综上，一个Trie类的初始化方法就很好写了：
```python
class Trie:
    def __init__(self):
        self.child = {}
        self.end = False
```

其他几个方法，也都是用一个指针扫描的套路。注意`search`和`startsWith`实现上的唯一区别在于判断扫描结束时的节点的`end`值。
其实之前的指针扫描部分的代码可以写一个共通的方法复用。