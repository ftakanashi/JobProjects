## 题目描述
将非负整数 num 转换为其对应的英文表示。

示例 1：
```
输入：num = 123
输出："One Hundred Twenty Three"
```
示例 2：
```
输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"
```
示例 3：
```
输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```
示例 4：
```
输入：num = 1234567891
输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

提示：
```
0 <= num <= 2^31 - 1
```

### 解法 分段处理 递归
基本又是一道面向testcase编程的题目…（注意这题的答案并不是标准的英语说法，实际上标准英语说法其中还涉及到比如and的使用，one的省略等，更加复杂

大体的思路框架还是相对比较好想到的。
观察几个示例的case之后发现，实际上可以按照英语计数的习惯，将数字分成三个一段，即thousand, million, billion这三个级别。
由于数字最大是`2**31 - 1`，所以计数节最大也就billion。

在分段之后，每段其实就可以当成一个999以内的数字进行处理了。
而对于这样一个数字，又该怎么求其表达呢？

首先，还是继续分段，把hundred单独拆出来。这步十分简单。
其次，对于剩下的两位数，则需要根据
- 是否能被10整除（若可以则要写`*ty`那种形式
- 是否是10-20间的数（`*teen`形式
- 是否是一位数

只要独立写出数字到字符串形式的映射，单独讨论上面几种情况即可。
而对于原数大于100的情况，实际上可以先求出其hundred部分，然后递归地求剩下两位数部分。

这么一来，一个用来处理999以内数字成字符串的工具函数就做好了。

接着回到外面，大体框架让num不断`num % 1000`以及`num = num // 1000`，然后处理，加上thousand, million, billion等后缀，拼接结果即可。

当然，其中细节稍微有些麻烦。当然此时已经没有什么难度了，如果能给出哪些testcase没过就更简单了，debug相关代码即可。
建议关注一下这几个特殊case：0, 100, 1000, 1000000

更多东西写在代码注释中了。