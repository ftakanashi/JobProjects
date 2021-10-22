## 题目描述
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：
- WordDictionary() 初始化词典对象
- void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
- bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
 

示例：
```
输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

提示：
```
1 <= word.length <= 500
addWord 中的 word 由小写英文字母组成
search 中的 word 由 '.' 或小写英文字母组成
最多调用 50000 次 addWord 和 search
```

### 解法 字典树 + DFS
一看就知道肯定要有字典树。
这题比字典树稍微难一点的地方在于要求搜索操作支持通配符`'.'`。
这就很容易想到用DFS搜索改造一下字典树探索过程就可以了。

简单来说，首先字典树的结构，以及`addWord`操作都和标准字典树没有区别。
另一方面，在`search`函数中，我们放弃原先字典树只搜索一条路径的办法，而是采用DFS的可回溯搜索的办法。

定义`dfs(node, pos)`，表示当前位于字典树的`node`节点时且正扫描到单词中下标为`pos`的字母。

显然，当`pos == n`时，那么就是搜索完了，返回`node.end`作为结果即可。
另一方面，这里还需要讨论的是`word[pos]`的情况。
如果是普通字母，就按照普通字典树搜索，查看相关子节点是不是None。
若是通配符，那么就要对所有可能的下一个子节点做递归探索。此时就要依次调用`dfs(child, pos+1)`了。这些调用中只要有一个是True，那么就返回True。
反之若一个都不能成功，就返回False。

综上，一道简单地结合了Trie和DFS的题目。