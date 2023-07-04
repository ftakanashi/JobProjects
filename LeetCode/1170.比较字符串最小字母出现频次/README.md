## 题目描述
定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。

例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。

请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。

示例 1：
```
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
```
示例 2：
```
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
```

提示：
```
1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j]、words[i][j] 都由小写英文字母组成
```

### 解法 哈希表 二分查找
这题又是一道只要读懂了题意就不难的题目…

题意比较绕，首先是理解`f`函数。其实就是对某个字符串，统计每个字母出现的频次，然后取所有出现过的字母中字典序最小的那个的频次作为返回结果。
因此可以先将`f`函数给定义出来。
一个最简单的做法是counter取频次后排序所有key，取最小值。
这样的话相当于会遍历一遍再加排序，整体复杂度可能较高。也可以一次遍历，遍历时记录频次以及当前遇到过的最小字典序字母，如下：
```python
def f(s):
    min_ch = "{"
    cnt = Counter()
    for ch in s:
        if ch < min_ch:
            min_ch = ch
        cnt[ch] += 1
    return cnt[min_ch]
```

然后来看`queries`和`words`是怎么回事。
其实题目要求的是`queries`中的每个`q`对应整个`words`的一对多关系。处理每个`q`时，不难看出`words`是相对固定的。所以可以先行将所有`words`
对应的`f`函数返回值求出后排序。

之后每个`q`可以算出`f(q)`，然后再到`words`中去找有多少个大于这个值的数量即可。
由于`words`已经排序，所以可以使用二分的方法来找。具体的，`bisect.bisect(words, q)`可以找出`words`中有多少个大于等于`f(q)`的值。
自然`len(words)`减一下就是最终答案了。