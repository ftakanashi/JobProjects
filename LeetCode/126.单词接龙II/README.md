## 题目描述
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：

每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。

示例 1：
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```
示例 2：
```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
```
 

提示：
```
1 <= beginWord.length <= 7
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有单词 互不相同
```

### 解法1（待优化） BFS
抱着试一试的心态写了个比较暴力的BFS，没想到还AC了…
当然还有很多优化的空间，这里姑且先记录一下自己的做法。

首先，很明显这道题的本质是一个图中求最短路径的问题。
稍微麻烦的一点在于，题目要求求出所有的最短路径，且要求给出详细路径。

求最短路径无疑可以用BFS。

于是首先，构建图。写构建图的代码的时候，没看到`LC.127`的优化，所以没有用到虚拟节点之类的技巧。
简单粗暴地，直接定义了一个方法，扫描任意两个单词的各个位置，如果有且只有一个位置不同，就返回True，否则False。

构建完图之后，就是BFS了。从beginWord出发，进行BFS扫描。
注意因为要求所有可能的路径，所以不能从queue中拿到一个node，如果其在seen中就直接continue。
然而这么做的后果是可能会带来很多重复结果，于是我简单粗暴地将结果收割容器换成了set…

另一方面，因为只需要最短路径，所以在初次确认到一条路径之后，直接将其的长度设置为最短路径长度，并且继续扫描。
当后续扫描出来的路径长度等于这个最短路径长度，那么这路径还是可以收割的。
否则，就说明BFS的扫描已经超过了限度，因为只要求最短路径，所以可以直接break掉了。

以上就是比较简单粗暴的BFS思路，幸运的是可以直接AC…