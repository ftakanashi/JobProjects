## 题目描述
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

示例 1：
```
输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
```
示例 2：
```
输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
```
示例 3：
```
输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。
```

提示：
```
1 <= chars.length <= 2000
chars[i] 可以是小写英文字母、大写英文字母、数字或符号
```

### 解法 双指针
用栈的解法这里就不说了，因为题目直接要求用常数空间做了。

题目给的提示也很明显，既然要在数组内原地修改，那么双指针就不可避免了。
具体的，一个快指针做整体的扫描，并且扫描过程中应该取记录那些连成一片的字符串span，并将相关内容用慢指针写在数组的前段部分。

由于长度为1的span（即单个字母）不用写数字，所以慢指针总是比快指针更慢，不会超越，因此不用考虑特殊情况。

具体的算法，在`while j < n`这个循环进去后，我们默认当前`j`处于一个span的开始位置，并记录这个位置。
接着`while j < n-1 and chars[j] == chars[j+1]`自增`j`。当循环结束时，`j`处于span的结束位置。

只要这两个位置间的长度大于1，就将数字挨个写进`i`的位置。

在那之前，也别忘了还要写字母本身，这里可以用`chars[i] = chars[j]`来做。

总体来说，算法本身除了需要注意一些细节外，整体不难。就是一个模拟的过程。