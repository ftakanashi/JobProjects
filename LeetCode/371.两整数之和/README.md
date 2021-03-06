## 题目描述
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:
```
输入: a = 1, b = 2
输出: 3
```
示例 2:
```
输入: a = -2, b = 3
输出: 1
```

>注意，本题目默认是给Java等语言设计，其所有testcase的输入输出都在32位带符号整数范围内

### 解法 位运算
首先是方法。显然既然不能用加减符号，那么只能位运算了。

对于两个二进制的数来说，
各个位数相加只可能有四种情况：
```text
0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 0 (进位)
```
前三种的好说，第四种由于要进位所以需要特殊处理。

一种朴素的思路是逐位加和并且记录进位模拟运算。这里介绍一个更快的办法。
注意到上述四个式子如果抛开进位操作不管，那就是异或运算。

比如4和5相加，二进制下先计算异或可以得到`001`。其中第一个0其实是要进位的。
为了找到哪些位置要进位，
接下来，也是神之一笔，计算4 & 5。要进位的地方只发生在1和1配对的地方，即和结果是1的地方。

不过真正+1的位置都是在要进位的地方的左边一格，所以还要将和结果左移一位。

至此，方法就OK了。如果使用Java等语言做答，那么可以写出如下代码：
```text
class Solution {
    public int getSum(int a, int b) {
        int res;
        int carry;
        if(b == 0){
            return a;
        }
        res = a ^ b;
        carry = (a & b) << 1;
        return getSum(res, carry);
    }
}
```

但问题是Python不能直接这么干，因为Python的实现机制的问题，上述左移操作永远没有尽头。
其他语言的int，比如32位，至多左移32次就会变成0，而python的永远不会。

这么一来，稍微试一下就明白，比如1和-1相加，写一下其二进制过程就知道，carry永远没办法变成0，因此无限循环。

解决办法就是手动模拟32位整数的运算。
模拟点主要在两个。

第一个，计算异或以及和运算的时候，排除32位以及更高位的影响。
具体做法就是将所有结果都进行对2**32的取余 （相当于每次计算结果只取最后32位作为有效位数）

第二个，输出结果时，如果32位是1，说明输出的是负数，但是Python中默认int位数更大，因此将其识别成一个很大的整数，
需要做一个转化。

#### 关于这个转化过程
这个转化过程也比较有意思。比如我想输出-2。
此时其32位二进制应该是`1111...10`。一般来说我们可以"减一取反"来获取其绝对值。
但是别忘了Python中其保存的实际上是`0000....00 1111...10`，前面还有好多多余0。
如果直接减一取反，前面那些0会被取反成1。就不对了。

所以这个转化过程也要模拟32位整数的转化，首先采取对2**32取余的方式取出这个数的后31位，
如`0000...00 1[111...10]`，中括号内的是取出来的。
然后将其减一取反。注意取反也不能直接用`~`运算符，因为一旦你把上面这部分取出来保存到一个int变量里，python又直接把他解释成比32位大的了。

这里取而代之的办法是，将其与2**32-1进行异或运算。
**其实不难发现，n位整数的取反操作，其实就是和2^n-1的异或的结果**

另外关于减一，如果想严格遵守题目，不想用减号，那么可以这样：
将取出来的后31位先和2**32-1异或。此时由于两个数字的高位都是一片0，所以并不会出叉子。
然后再整个取反，此时利用`~`运算符，python会把高位也都变成1，自然就输出了负数。
这也是一个python中int数据进行符号转换的小技巧吧。
上述方法写在了代码的注释里。

>以上解释还是有点费解。JZ65的题解是我自己从零撸出来的，可能好懂一些。