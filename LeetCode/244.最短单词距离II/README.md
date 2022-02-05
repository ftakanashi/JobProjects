## 题目描述
请设计一个类，使该类的构造函数能够接收一个字符串数组。然后再实现一个方法，该方法能够分别接收两个单词，并返回列表中这两个单词之间的最短距离。

实现 WordDistanc 类:
```
WordDistance(String[] wordsDict) 用字符串数组 wordsDict 初始化对象。
int shortest(String word1, String word2) 返回数组 worddict 中 word1 和 word2 之间的最短距离。
```

示例 1:
```
输入: 
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
输出:
[null, 3, 1]

解释：
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // 返回 3
wordDistance.shortest("makes", "coding");    // 返回 1
```

注意:
```
1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] 由小写英文字母组成
word1 和 word2 在数组 wordsDict 中
word1 != word2
 shortest 操作次数不大于 5000 
```

### 解法 哈希表 双指针
这题的基本思想和上一题`LC.243`还是一样的。
只不过由于会调用`shortest`多次，如果每次调用都从头扫描一遍整个列表就略显低效了。

这里，我们可以实现通过一个`defaultdict(list)`将所有单词以及其下标按照顺序对应起来。
这样，每调用一次shortest的时候，就可以直接找到两个升序的下标列表，然后只要在这两个列表上设置双指针，
以类似的规则遍历一遍即可。

特别的，当某一个列表指针到头遍历完成时，另一个列表可能还没遍历完。
但是因为求的是最短距离，所以即便另一个列表还没遍历完，后面的所有更远的下标距离都是更大的，没必要像归并排序那样处理尾声。