## 题目描述
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：
```
MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。
```
示例：
```
输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False
```

提示：
```
1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写英文字母组成
dictionary 中的所有字符串 互不相同
1 <= searchWord.length <= 100
searchWord 仅由小写英文字母组成
buildDict 仅在 search 之前调用一次
最多调用 100 次 search
```

### 解法 字典树 + DFS
一道比较有意思的题目，不过我这个解法并不是很优秀，应该存在更加优化的办法。

简单来说，要从字符层面判两个字符串的相似性，又是先存储再搜索的pattern，所以很容易想到用字典树作为容器来保存`buildDict`过程中预存入的信息。

另一方面，题目要求search的时候单词要和预存入的单词恰好差一个字符，这个就稍微有点麻烦了。
首先我们还是按照一般的思路，用DFS来进行搜索。

只不过在搜索过程中，碰到某个字符和当前搜索的字符不一样时，我们就需要考虑，是否恰好是题意中所说的那个不一样的字符。
于是我们在dfs函数中引入一个flag开关。这个开关用来表示之前的搜索中有没有遇到过不一样的字符。

这样，进入一层dfs的时候，我们就可以按照这个开关分类讨论。
当flag还是True的时候，说明之前还未遇到过不同的字符，于是我们考虑遍历当前节点所有非空的child，不论其是否与当前遍历到的字符相同。
当然若不同，则需要将flag置False再进入下一层dfs。

当flag是False的时候就简单了，我们只需要找和当前遍历字符相同的child进入即可。

进入下一层dfs后，只要下一层dfs能够返回True，表示能够至少找到一个和searchWord差且只差一个字符的预存单词，所以整个dfs可以返回true。

最后还需要注意，若searchWord恰好是某个预存单词，且预存单词中不存在和其只差一个字符的其他单词。此时根据题意应该返回False。
此时dfs也能走到最后，那么就不能简单的以`len(searchWord) == pos and node.end`的形式来判断dfs的终结。
还得加上一个`not flag`，以表示之前至少发生过一次字符替换。