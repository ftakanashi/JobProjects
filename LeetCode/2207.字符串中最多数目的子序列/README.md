## 题目描述

给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。

你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。注意，这个字符可以插入在 text 开头或者结尾的位置。

请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。

子序列 指的是将一个字符串删除若干个字符后（也可以不删除），剩余字符保持原本顺序得到的字符串。

示例 1：
```
输入：text = "abdcdbc", pattern = "ac"
输出：4
解释：
如果我们在 text[1] 和 text[2] 之间添加 pattern[0] = 'a' ，那么我们得到 "abadcdbc" 。那么 "ac" 作为子序列出现 4 次。
其他得到 4 个 "ac" 子序列的方案还有 "aabdcdbc" 和 "abdacdbc" 。
但是，"abdcadbc" ，"abdccdbc" 和 "abdcdbcc" 这些字符串虽然是可行的插入方案，但是只出现了 3 次 "ac" 子序列，所以不是最优解。
可以证明插入一个字符后，无法得到超过 4 个 "ac" 子序列。
```
示例 2：
```
输入：text = "aabb", pattern = "ab"
输出：6
解释：
可以得到 6 个 "ab" 子序列的部分方案为 "aaabb" ，"aaabb" 和 "aabbb" 。
```

提示：
```
1 <= text.length <= 105
pattern.length == 2
text 和 pattern 都只包含小写英文字母。
```

### 解法 贪心 一次遍历
题目看起来似乎很复杂，但是实际上并没有那么困难。只需仔细审题即可。
注意到，pattern的长度一定是2，这就大大简化了难度。

很容易发现，text中其实所有非pattern中那两个字母的其他字母都是干扰项，因此，假设pattern是`ab`的话，
text可以看做一个 `a, b, x` 三个字母组成的字符串。

比如示例1就是 `axxcxxc` 。
再次审题，题目要求求的是所有可能的子序列，这也就意味着在不插入额外字符的情况下，就已经可以形成两个 `ac` 子序列了。
那么如果新插入一个`a` ，怎么样才能让子序列数量最大化呢？
显然，为了可以和所有text中的`c`进行配对，这个`a`可以放在整个序列的最左边。

同理，如果要插入`c`，则应该放到整个序列的最右边。

如此，我们便得到了规律，首先是简化text，然后尝试将 `pattern[0]` 插入到最左边， `pattern[1]` 插入到最右边。
计算两种情况下的子序列数量即可。

那么子序列又该如何计算呢，这可以一次遍历搞定。
遍历过程中，计数统计 `pattern[0]` 和 `pattern[1]` 出现的次数。
此外如果碰到`pattern[1]`，则之前所有出现过的`pattern[0]` 都可以和其配对组成一个子序列，应当对答案进行更新。

在不考虑额外插入的情况下，一次遍历便可得到text本身可贡献的子序列数量。
接着遍历过程中我们也得到了所有 `pattern[0]` 和 `pattern[1]` 出现的次数，
选两者中较大的一方，比如 `pattern[0]` 出现次数较多，此时往text尾部插入`pattern[1]`比较合算。

最后还有个特殊点需要考虑，即 `pattern[0] == pattern[1]` 的情况。
此时虽然也可整合到上述逻辑中，但是稍微难懂一点。
我建议可以对这个特殊情况单独考虑。当 `pattern` 是 `aa` 形式的，那么就意味着答案就是 text中 `a` 出现次数 + 1的字母，
可形成的子序列个数。