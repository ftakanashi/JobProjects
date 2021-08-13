## 题目描述
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。

序列中最后一个单词是 endWord 。

每次转换只能改变一个字母。

转换过程中的中间单词必须是字典 wordList 中的单词。

给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。

示例 1：
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
```
示例 2：
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
```

提示：
```
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
```

### 解法 BFS + 虚拟节点建图
一道很典型的BFS题。与其说难点是想到BFS，还不如说难点是如何构建图。

很自然的可以想到，将每个单词视作一个节点；每一次操作视作一个边，连接了变化前后的两个单词。
这样，只要构建出图，然后在图中进行BFS，搜到的第一条通路就是最短路径了。

思路也确实正确，但问题在于构建图的过程。
如果按照朴素思想，直接遍历所有词的两两组合，然后检查是否有边相连，复杂度有些高。
这里就有个很巧妙的办法，使用虚拟节点。

具体的，将某个单词的每个字母轮流改成一个特殊字符如`*`，并将这些虚拟单词也放入图中，
并将原单词和虚拟单词相连。
如单词`hot`，三个虚拟节点分别是`*ot`, `h*t`, `ho*`。

这么做的好处是，通过虚拟节点，只要在`O(nw)`(n是单词数，w是单词长度)的时间内就可以构建出完整的图了。
比如上面`hot`，而`hit`直接通过`h*t`与之相连（当然有了虚拟节点之后并不是直接相连了，但是拓扑逻辑没有变）

BFS部分很简单，就不说了。
值得一提的是，建图还需要将所有单词和虚拟单词都映射成ID。这里我额外实现了一个WordMap类，以及类的两个方法addWord和getWord
来实现这个功能。

最后，BFS结束后，得到的距离，包含了虚拟节点，要将其去除。
具体来说，因为虚拟节点在每两个原单词相连的边上都有，所以正确答案应该是带虚拟节点的遍历步骤数除以2再+1。
