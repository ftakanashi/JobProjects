## 题目描述
给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

 

示例 1：
```
输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
```
示例 2：
```
输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]
```
示例 3：
```
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
```

提示：
```
1 <= s.length <= 104
s 由小写英文字母组成
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] 由小写英文字母组成
```

### 解法 滑动窗口
先审题。题目的意思是，从s中找出一个`len(words) * len(words[0])`长度的子串，使得其恰好是`words`中各个单词按某个全排列得到的串联。
且一个比较方便的条件是`words`内的各个单词长度相同。

不得不说，题目的示例太迷惑性了…
看了三个示例，第一个就想到了，这不就是把字符层的滑窗变成了单词层的滑窗么。
比如把bar, foo, the, man分别定义为ABCD，那么示例3的输入就是
`ABBACBAD`。然后题目就是让你从中找出连续的三个字母，使得其是ABC的一个排列。

显然，可以用滑窗来做。
滑窗滑动的算法如下:(注意下面的算法都是基于上述单词视角，比如加减1的这个1指一个单词长度单位而非真的长度1)
```python
res = []
counter = Counter(words)
window = Counter()

l = r = 0
while r < len(s):
    window[s[r]] += 1
    if s[r] not in counter:
        l = r = r + 1
        continue
    if window[s[r]] > counter[s[r]]:    # 某个单词在窗口中超额了,则移动左边界使其不超额
        while window[s[r]] > counter[s[r]]:
            window[s[l]] -= 1
            l += 1
    r += 1
    if r - l == len(words) * len(words[0]):    # 整体长度达标，收割结果。同时为了不错过任何结果，左边界保守地移动一格
        res.append(l)
        window[s[l]] -= 1
        l += 1
```

但是上述算法提交了之后，发现并不通过。
仔细一看，发现是自己傻逼了，被示例迷惑，漏掉了一格很重要的细节。

所有示例默认都从位置0开始扫描，判断是否存在合理的解。所以下意识地就将所有操作看成单词层面的。
但是，比如在示例3的输入字符串最前面加上一个x。
这样输出答案个数应该不变（虽然答案的值不再是3的倍数了），但是从0开始进行扫描将无法获得任何答案。

基于这个错误，我们应该从0，1，2三个位置分别出发进行扫描，然后将三套滑窗得到的结果全合并起来作为最终结果。
而从位置3出发的扫描其实和从位置0出发的扫描等价。

更一般的，对于`w_len = len(words[0])`的情况，我们需要从`range(w_len)`这些位置开始扫描。
而每个扫描都可以套用上述滑窗的算法。因此将上述滑窗算法包装成一个子函数`search_from(start: int) -> List[int]`。

最终将`w_len`个结果列表给合并起来作为最终返回。