## 题目描述
我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。

注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。

示例 1：
```
输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
```
示例 2:
```
输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
```

提示:
```
n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target <= 15
stickers[i] 和 target 由小写英文单词组成
```

### 解法 记忆化搜索
这题其实没那么多小九九，直接暴力搜索即可。

具体来说，显然每个sticker都对应了一个counter，其中记录了各个字母在sticker中的数量。
而target又是一个合集。只需要选用一部分sticker，其counter的并集能够包含target的集合即可。

既然用暴力，那么显然过程是依次遍历sticker，尝试使用某个sticker来填充target。将这个过程抽象为一个dfs函数。
于是target中的一部分字母被填充，接下来要尝试填充剩余部分，于是就需要dfs剩余部分。

实际实现中，可以使用二进制位来表示target中的每个字母的填充情况。因此dfs函数的参数可能只是一个数字mask（其二进制位表示填充情况）。

在dfs过程中，按照上述描述遍历sticker。针对一个固定的sticker，遍历target中每个字母。
只要某个字母在mask中的位仍是1且对应sticker的counter中也还大于0，那么就说明其可以被填充到target中，
于是更新mask与sticker的counter。

如此，直至内层遍历target各个字母的循环完成，此时若更新后的mask小于最初的mask，说明选取这个sticker是有作用的。
因此可以继续探索更新后的mask的情况，并且将dfs结果+1。

以上dfs过程由于没有借助外部数据并且参数是一个int，所以可以直接加cache记忆化。
