## 题目描述
给定一个字符串数组 wordDict 和两个已经存在于该数组中的不同的字符串 word1 和 word2 。

返回列表中这两个单词之间的最短距离。

示例 1:
```
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
输出: 3
```
示例 2:
```
输入: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
输出: 1
```

提示:
```
1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] 由小写英文字母组成
word1 和 word2 在 wordsDict 中
word1 != word2
```

### 解法 双指针 一次遍历
按照题意，整个列表中，会有若干位置上单词是word1或者word2，
而在扫描过去的过程中分可以维护两个指针p1和p2指向当前扫描到的最新的word1和word2的位置。

根据题意，最近的两个单词，其两个位置中间必然没有另一个word1或者word2，所以可以在一次遍历的过程中找出最短的距离。