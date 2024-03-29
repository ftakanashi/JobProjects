## 题目描述
单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：

words.length == indices.length

助记字符串 s 以 '#' 字符结尾

对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等

给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。

示例 1：
```
输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
```
示例 2：
```
输入：words = ["t"]
输出：2
解释：一组有效编码为 s = "t#" 和 indices = [0] 。
```

提示：
```
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] 仅由小写字母组成
```

### 审题
注意题中的一个细节，所有单词能在压缩串中被找到，且找到时其最后一个字母后面一定是#。

对于示例1，time, me, bell三个单词，之所以压缩字符串是`time#bell#`，是因为me恰好是time的后两个字母。

换言之，如果me换成了tim，那么`time, tim, bell`三个单词的压缩字符串将可能是`time#tim#bell#`。

即，只有一个词是另一个词的严格的后缀时，才能将其压缩到另一个词中。

### 解法 字典树
既然牵扯到字符串的前后缀，很容易就想到了用字典树了。
因为是后缀，所以就只需要维护一个倒序字典树就可以了。

具体的，我们创建一个字典树，然后将所有单词扫描，并倒着维护到字典树中。

比如示例1的数据，维护完之后字典树大概长这样：
```text
    root
   e    l
   m    l
   i    e
   t    b
```
即两条触手。

值得一提的是，为了表示`me`也在字典树中，上树中的左边的`m`节点处，应该有`end=True`这个属性。
当然这题并没有要求具体找出所有单词的边界，因此不实现end机制也无所谓。
我的代码中为了方便记忆，还是将end写了进去。

有了树之后，一切就好办了。
求的是压缩串的长度，换言之就是这棵字典树中的路径总和罢了。（即到达每个叶子节点走的步数的总和，注意重复路径要算两次，比如若输入是`time, lime`
构建树之后只在倒数第二层分叉，但是压缩串的长度却是`5+5=10`。