## 题目描述
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

示例 1：
>输入：s = "abcd", t = "abcde"
>
>输出："e"
>
>解释：'e' 是那个被添加的字母。

示例 2：
>输入：s = "", t = "y"
>
>输出："y"

示例 3：
>输入：s = "a", t = "aa"
>
>输出："a"

示例 4：
>输入：s = "ae", t = "aea"
>
>输出："a"

提示：
- 0 <= s.length <= 1000
- t.length == s.length + 1
- s 和 t 只包含小写字母

### 解法1 哈希表计数
先分析s，把其中的字母:计数关系维护进一个哈希表。
然后再分析t，依次减去哈希表中的计数。最终留下来数目不是0的就是所求字母。

### 解法2 位运算
参考LC.136只出现一次的数字。
这里无非是将数组分成了两半。依次扫描s和t中每一个字符。

由于t只比s多出一个字符，说明其余字符都是两两配对的。

因此采用连续异或运算进行那个字符的抽出。

注意异或运算两边只能是数字，所以对字符要做ord和chr工作。