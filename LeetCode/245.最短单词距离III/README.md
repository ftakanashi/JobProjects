## 题目描述
给定一个字符串数组 wordsDict 和两个字符串 word1 和 word2 ，返回列表中这两个单词之间的最短距离。

注意：word1 和 word2 是有可能相同的，并且它们将分别表示为列表中 两个独立的单词 。

示例 1：
```
输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
输出：1
```
示例 2：
```
输入：wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
输出：3
```

提示：
```
1 <= wordsDict.length <= 105
1 <= wordsDict[i].length <= 10
wordsDict[i] 由小写英文字母组成
word1 和 word2 都在 wordsDict 中
```

### 解法 双指针 一次扫描
基本套路还是和`LC.243`一样。
这题只是单纯地引入了word1和word2相同的情况。

所以只需要分类讨论即可。
即，若word1和word2不同，那么直接使用`LC.243`的解答方法即可。实际上代码里我就是直接copy了`LC.243`的代码。

对于word1和word2相同的情况，那么就是一个简单的一次扫描了。
我更偷了个懒，先扫描一遍原列表把所有该单词的下标取出来，然后扫描一遍这个下标列表，把其中最小的差值取出即可。