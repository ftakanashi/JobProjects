## 题目描述
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

操作 1：交换任意两个 现有 字符。
例如，abcde -> aecdb
操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。

示例 1：
```
输入：word1 = "abc", word2 = "bca"
输出：true
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"
```
示例 2：
```
输入：word1 = "a", word2 = "aa"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```
示例 3：
```
输入：word1 = "cabbba", word2 = "abbccc"
输出：true
解释：3 次操作从 word1 获得 word2 。
执行操作 1："cabbba" -> "caabbb"
执行操作 2："caabbb" -> "baaccc"
执行操作 2："baaccc" -> "abbccc"
```
示例 4：
```
输入：word1 = "cabbba", word2 = "aabbss"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```

提示：
```
1 <= word1.length, word2.length <= 105
word1 和 word2 仅包含小写英文字母
```

### 解法 哈希表 排序
这题倒是有点意思。

首先看清楚题意，两种操作都是可以做若干次的。

对于第一种操作，只需要保证两个字符串中每种字符的都一样，那么不论怎么互换位置都是符合要求的。

而对于第二种操作，则要求的是字母出现的频度集合是一致的。

综合考虑这两种要求，其实一个比较简单粗暴的判断方式就是。
首先对两个字符串各个字母出现的频度进行统计。
然后要求 1.两个字符串中出现的所有字母都是相同的，因为即使是第二种操作也要求是出现过的字母互换频度。2.则是所有字母出现的频度的分布是相同的。
这是方便第二种操作。

综合起来来说，就是这么个逻辑：
```python
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        ch_counter1 = Counter(counter1.keys())
        times_counter1 = Counter(counter1.values())
        ch_counter2 = Counter(counter2.keys())
        times_counter2 = Counter(counter2.values())
        return ch_counter1 == ch_counter2 and times_counter1 == times_counter2
```

事实上上述代码直接AC，并且效率很高（应该是Counter的优化好