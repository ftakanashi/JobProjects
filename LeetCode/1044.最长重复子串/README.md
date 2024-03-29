## 题目描述
给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

示例 1：
```
输入：s = "banana"
输出："ana"
```
示例 2：
```
输入：s = "abcd"
输出：""
```

提示：
```
2 <= s.length <= 3 * 10^4
s 由小写英文字母组成
```

### 解法 threshold二分 Rabin-Karp算法 + 滑窗 + 哈希碰撞优化
这个解法的思路链有点长，但是并不难，沉住气一点点看吧。

首先说一下大体的思路框架。
应该意识到的一点是，题目中提到的"最长长度"是一个具有二分性的值。换言之，若存在重复子串，则必然存在一个长度`0 < L < n`，使得
所有小于`L`的长度必然有对应的重复子串（其实拿`L`长度重复子串的一部分出来就行了），大于`L`的长度必然没有重复子串。
比如`banana`这个例子，我们知道`L`是3。
那么`L`是2的重复子串有没有？肯定有。`L`是3时的答案是`ana`，那么这个串的长度为2的子串`an`或者`na`肯定也是整个字符串的长度为2的重复子串。
而`L > 3`的时候就没有符合条件的子串了。

既然这个值具有二分性，那么显然可以用一个二分查找来寻找那个最大的L值。
这就是一个所谓的threshold二分了。

我们知道threshold二分的关键在于定义一个合理高效的check函数。
这题里，函数`check(mid)`要做的工作是检查原串中是否有长度恰好为`mid`的重复子串。
显然，如果单纯做一个带哈希的暴力扫描的话，复杂度会是`O(nL)`的。
这里，可以使用Rabin-Karp算法对字符串进行编码从而进行重复性的判断。

#### Rabin-Karp算法
这个算法的功能是通过对等长字符串的哈希性编码，从而快速搜索字符串的存在性。
原理十分简单，当所有字符串等长且字符种类有限且不多时，直接将每个字符视作一个数，而将固定排列的一个字符串视作一个特定进制的数。

最常见的，比如所有字符串都由小写英文字母构成时。我们可以将所有字符串视作一个26进制数。
比如"bca"，就可以表示为`1 * 26^2 + 2 * 26^1 + 0 * 26^0`。
当然因为英文字母一共26个，将a-z编码成0-25之后，用26进制是一个最经济的进制。
如果你想使用更高的进制比如50进制之类的，也OK，只不过那样会有大量的空缺哈希编码，导致一定程度的浪费。

注意，该算法只适用于等长字符串的编码。若不等长，比如`a`和`aa`在上述编码条件下编码相同，无法分辨，属于是哈希碰撞了。 

（完）

讲回本题。
我们注意到，在等长的情况下，任意两个字符串经过Rabin-Karp算法编码后如果编码一致，那么两个字符串也必定一致。
通过这个性质可以去做子串重复性的判断。

如果针对每个子串都按字符扫描构建编码那么复杂度还是`O(nL)`的。
这里，我们采用滑动窗口的办法。
比如对于`banana`，我们寻找`L`为3的子串时，首先编码得到`ban`的编码是`1 * 26^2 + 0 * 26^1 + 13 * 26^0`。
将其加入一个set。
接着窗口右移，此时我们不重新计算`ana`的编码，而是将上个编码减去`1 * 26^2`后再乘以26，再加上`a`的编码。即
```python
code = code - (1 * 26^2)) * 26 + encode(a)
```
如此，便在O(n)的时间内就可以找出所有长度为L的子串的编码。结合哈希集，就可以判断子串的重复性啦。

至此，基本的算法就有了。实际上我也实现了出来，但是发现会超时。
这版代码写在了main的注释中。

分析一下，发现超时的原因主要可能在于，因为s可能很长，所以L可能很长。
当L很长的时候，进行大数的计算比较耗时（虽然Python没有溢出的危险，但是仍然耗时）
因此我们需要考虑如何优化。

一个最简单的思路，就是对编码过程进行取余。这实际上也是Rabin-Karp算法在实现过程中经常会用到的一个技巧。
但是一旦取余，就会增加哈希碰撞的可能性。为了杜绝这种可能，我们采用双哈希法进行优化。
简单来说，我们放弃使用单一的26进制，而是采用随机化的两个进制以及两个进制各自的随机化的两个模。
针对一个字符串，我们通过两种进制+模，分别编码成两个码，只有这两个码都完全一致，才能判断原字符串一致。
（不得不说一句，妙啊

最后，因为题目要求出某个最长长度的重复子串具体内容，所以二分的check函数不能单单返回True或者False。
我们可以让他返回发现重复子串时的具体位置，结合这轮check的长度mid，就可以确定一个子串的具体内容啦。

更多解释写在代码注释中。

P.S. 有更高级的解法比如后缀数组啥的，不懂就不多说了…