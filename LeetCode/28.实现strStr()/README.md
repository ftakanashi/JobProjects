## 题目描述
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。

如果不存在，则返回  -1。

示例 1:
>输入: haystack = "hello", needle = "ll"
>
>输出: 2

示例 2:
>输入: haystack = "aaaaa", needle = "bba"
>
>输出: -1

说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

### 审题
简而言之，一句话就是实现字符串的find方法。

废话解法就是一句话`return haystack.find(needle)`。

然后重现这个方法详细的话，最先能够想到的是线性扫描，这里也不多说了。

下面介绍两种比较有意思的解法。

### 解法1 滑窗 + 哈希
线性扫描的过程，外层扫描感觉挺合理的，但是每次内层扫描也要花线性时间，感觉略微有点拉胯。

那么有没有什么好办法可以用常数时间完成两个字符串的对比呢？

想到可以对比哈希值来确定。但是这里的哈希值不能是传统意义上的MD5值等，因为用那些哈希值的话到头来，还是要花线性时间
读取整个串然后哈希化。

这里说的哈希值，是更广泛意义上的哈希值，并且为了做到能在常数时间内完成计算，设计哈希值如下：

注意到，题中涉及到的字符串只有小写字母组成。
因此我们可以把字符串看作是一个26进制的数。

这样的数和字符串本身是一一对应的。

比如"fra"，其值就是
`5 * 26^2 + 17 * 26^1 + 0 * 26^0`

算法就是，先计算出needle的hash。

然后计算`haystack[:m]`的hash。如果其等于needle的hash，则直接返回0。

否则，向右滑动haystack的窗口。显然，第一步会删掉haystack[0]然后加入haystack[m]。
这个过程的hash化就是减去`h0 * 26^(m-1)`后本体乘以26，然后加上`hm`。

如此，我们就在O(1)的时间内求得了新窗口子串的hash值。

这个滑窗继续往右滑，某位置其hash值和needle一致就返回位置，到头了也没有就返回-1。

>另外可能需要注意的一点是，由于基数26挺大的，当字符串一长，在传统语言中很有可能面临溢出的风险。
>
>此时可以考虑采用取模的办法。即所有计算结果都对一个大数比如2**31取模作为结果。

### 解法2 KMP算法
这次再审视一下外层扫描的合理性。这也是KMP算法的大初衷。

即，根据needle字符串本身的性质，可以做到不是每次都前进一步，
而是跳着前进着扫描haystack。

具体KMP算法的解析请看书本或者PlayGround里的内容。