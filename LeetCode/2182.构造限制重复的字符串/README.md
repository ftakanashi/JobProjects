## 题目描述
给你一个字符串 s 和一个整数 repeatLimit ，用 s 中的字符构造一个新字符串 repeatLimitedString ，使任何字母 连续 出现的次数都不超过 repeatLimit 次。你不必使用 s 中的全部字符。

返回 字典序最大的 repeatLimitedString 。

如果在字符串 a 和 b 不同的第一个位置，字符串 a 中的字母在字母表中出现时间比字符串 b 对应的字母晚，则认为字符串 a 比字符串 b 字典序更大 。如果字符串中前 min(a.length, b.length) 个字符都相同，那么较长的字符串字典序更大。
 

示例 1：
```
输入：s = "cczazcc", repeatLimit = 3
输出："zzcccac"
解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。
字母 'a' 连续出现至多 1 次。
字母 'c' 连续出现至多 3 次。
字母 'z' 连续出现至多 2 次。
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。
该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。
注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
```
示例 2：
```
输入：s = "aababab", repeatLimit = 2
输出："bbabaa"
解释：
使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。 
字母 'a' 连续出现至多 2 次。 
字母 'b' 连续出现至多 2 次。 
因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 
该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。 
注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。
```

提示：
```
1 <= repeatLimit <= s.length <= 105
s 由小写英文字母组成
```

### 解法 贪心 堆
思路的还是比较明显的，我们维护一个堆，从中随时可以拿到当前字母储备中字典序最大的字母即可。
当然拿出来之后还不能立刻加到ans后面，还得判断ans当前是否已经有连续的数个相同字母了。

所以整体的算法就是，维护好一个堆。堆的每一个元素是一种字母，以及其剩余计数。
为了利用heapq，我在实现中堆中元素是一个三元组 `(ord, cnt, ch)`，分别表示ord的相反数（用于维持反向字典序的堆序），剩余计数以及字母本身。

之后，从堆中pop出堆顶字母，看是否当前答案已经有连续 repeatLimit 个相同的这个字母了。
若否，则可以直接加到答案后面。将计数减一，若计数仍大于0则充回堆内。
若是，稍微复杂一些，在保存刚才pop出来的字母信息的同时，再从堆中pop一次（若堆空则直接返回）。此时pop出来的字母肯定不是刚才那个了，
所以可以放心直接加到答案中，计数减一并充回堆。最后别忘了把第一次pop的原封不动地充回堆里。

不过值得注意的是，其实上述基于堆的做法并不是最好的。
显然，当字符串给定之后，各个字符的出现频度等也都确定了，所以最方便的做法应该是直接排序就行了。