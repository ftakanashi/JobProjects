## 题目描述
给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。

示例 1：
```
输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
```
示例 2：
```
输入：words = ["cat","dog","catdog"]
输出：["catdog"]
```

提示：
```
1 <= words.length <= 10^4
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 10^5
```

### 解法 字典树 DFS
看到这道题的一个朴素解法是这样的：

首先由于所有的连接词都是由更短的词连接起来的，因此可以先将所有词按照长度从小到大排序。
接着扫描每个词，并将扫描过的词放入一个哈希集中。
针对扫到的当前词word，进行一次dfs。
dfs函数的输入是当前词的某个下标，而返回则是当前词中该下标开始到词尾的这个部分，能不能通过哈希集中若干个词连接而成。
显然，dfs函数的逻辑应该是像下面这样的：
```python
def dfs(pos):
    if pos == len(word): return True
    for i in range(pos, len(word)):
        if word[pos:i+1] in seen and dfs(pos + 1):
            return True
    return False
```

但是这种基于哈希的DFS并不能ac，会超时。
于是来（看）思（答）考（案）。
扫描到某个单词word时，我们下意识地通过哈希集来归纳前面的所有更短的单词，并试图从中找到能够拼接成word的一些子集。
这个问题，实际上是在一个字符串集中，不断查询某些串是否存在的过程。
这尼玛，有字典树啊。

于是，就有了用字典树代替哈希集的版本。
具体来说，扫到word时，其前面所有更短的单词都已经被插入到字典树中。
接着基于字典树进行DFS。
函数的大体逻辑不变，只是将`word[pos:i+1] in seen`这个判断换成一个字典树迭代的判断。

字典树相比于哈希集，其好处是当某个`word[x] (x是pos和i之间的某个位置)`字符不存在与字典树中时，
那么可以直接返回False，而不用再去尝试`x`和`i`之间的可能。
另外字典树不用频繁地切子字符串，可以节省一定时间。
总的来说，dfs函数大概长这样：
```python
def dfs(pos):
    if pos == len(word): return True
    node = root    # root是字典树根节点
    for i in range(pos, len(word)):
        if node.children[ord(word[i]) - ord('a')] is None: return False
        elif node.children[ord(word[i]) - ord('a')].end and dfs(pos + 1): return True
    return False
```

以这个dfs函数为中心，在外围建立扫描的逻辑即可。

另外还有一个小点，在外围，当确定某个词是连接词之后，这个词其实就可以不用加入字典树了。
因为后续如果有更长的连接词某个单元是本词的话，那么也可以是本词的那些更小的单元词构成。
换言之，扫描到word的时候，只有`dfs(0)`是False的情况，才需要将word加入字典树，否则就直接加入答案数组即可。
