## 题目描述

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
>输入: num1 = "2", num2 = "3"
>
>输出: "6"

示例 2:
>输入: num1 = "123", num2 = "456"
>
>输出: "56088"

说明：
- num1 和 num2 的长度小于110。
- num1 和 num2 只包含数字 0-9。
- num1 和 num2 均不以零开头，除非是数字 0 本身。
- 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

### 解法 以空间换时间的模拟
一般的竖式模拟这里就不说了，而且代码可能比较复杂。

这里提一种更加有意思的方案。

模拟竖式乘法的时候，显然一个很重要的问题就是处理进位。
在从个位向高位逐渐扫描相乘的过程中，要实时地递推维护进位系统。着实麻烦。

于是，想能不能先计算乘法，然后统一进位。这就要用到外部的一个数组作为存储媒介。

具体做法：
两个字符串相乘，假设一个长度为m，另一个为n。此时乘积结果的最长长度一定不会超过`m+n`，但也不会小于`m+n-1`（严格证明不做
但是可以脑补`10*10`和`99*99`）。

那么我们先初始化一个长度为`m+n`的数组，然后依次扫描所有两个数字中各个位数的乘积的组合可能性。然后保存到相应位置。

比如`123*456`的情况，个位的3和6乘积18保存到个位的位置。
个位乘十位的情况有两种，分别是`2*6`和`3*5`，两者相加得到27保存在个位乘十位的位置上。
以此类推…

最终可以得到一个类似于`[0, 4, 13, 28, 27, 18]`。

这个数组从右到左扫描，依次进位，取模10，最终得到`[0,5,6,0,8,8]`。
去掉最高位的0，剩下的组合起来就是答案了。

现在可以具体代码实现了。
具体写代码的时候注意一些细节，比如为了下标0作为个位的方便，两个数字可以先reverse。
这样`i`位和`j`位相乘的数字保存在结果的`i+j`位即可。当然得到的结果也是reverse的，最终返回前别忘了再reverse回来。

最终返回结果注意最高位是0的情况，以及两个数本身有一个为0的情况这些特别情况的处理。

>2021.02.21
>以上思想有点像做二进制加法时，不使用加号。而是采用
>```text
>a = x ^ y
>b = (x & y) << 1
>再递归地处理a,b，直到进位项和结果左移1的结果为0。
>```