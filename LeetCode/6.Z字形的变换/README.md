## 题目描述
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:
>输入: s = "LEETCODEISHIRING", numRows = 3
>
>输出: "LCIRETOESIIGEDHN"

示例 2:
>输入: s = "LEETCODEISHIRING", numRows = 4
>
>输出: "LDREOEIIECIHNTSG"
>
>解释:
>```
>L     D     R
>E   O E   I I
>E C   I H   N
>T     S     G
>```


### 解法1 数学法
不管具体字母，写一下n行时下标的情况：
```text
0              2n-2         4n-4
1          ... 2n-1         ...
2      n+1     2n
...  n         ...    ...
n-1            3n-3
```
这个时发现了规律，第一行以0开头，递增2n-2。
同样的最后一行以n-1开头，递增2n-2。

那么中间的行呢。其实可以发现，
对于第i行，其实从左到右依次是`s[i]`，`s[2n-2-i]`,`s[2n-2+i]`, `s[4n-4-i]`...

按照上述思路，不用额外空间，从扫描n个字符的角度来说时间也只是O(n)。

就可写代码了。