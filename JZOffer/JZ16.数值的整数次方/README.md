## 题目描述

实现函数double Power(double base, int exponent)，求base的exponent次方。

不得使用库函数，同时不需要考虑大数问题。

示例 1:
>输入: 2.00000, 10
>
>输出: 1024.00000

示例 2:
>输入: 2.10000, 3
>
>输出: 9.26100

示例 3:
>输入: 2.00000, -2
>
>输出: 0.25000
>
>解释: 2-2 = 1/22 = 1/4 = 0.25
 

说明:
- -100.0 < x < 100.0
- n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


### 解法 基于递归的周全考虑
其实看到这个题目第一眼，完全就是按照书上说的那样的。

```python
res = 1
for _ in range(n):
  res *= x
```

不过显然，这种做法没有提到如何进行负数次幂和0次幂的计算。因此，改第一版进行简单的分类讨论。

```python
def normal_pow(x, n):
    if n == 0:
        return 0 if x == 0 else 1
    res = 1
    for _ in range(n):
        res *= n
    return res

def myPow(x, n):
    if n >= 0: return normal_pow(x, n)
    else: return 1 / normal_pow(x, -n)
```

然而这版代码跑不过一些case比如
```python
0.00001
2147483647
```
超时了。
显然，问题出在了`normal_pow`函数上。这个函数是O(n)的。那么怎么样可以把他优化。

这个函数，因为工作就是计算正常情况的乘方，而实际上上面的方法做的是幂级别的加法。如果可以做幂级别的乘法，则效率可以大大提高。

更简单来说，比如`x^10`，其实是`x^5 * x^5`。只要求出`x^5`，那么第二个`x^5`就不用再求一遍了。

基于这个思路，可以写出式子如下：
```text
x^n = x^(n/2) * x^(n/2) ... n是偶数
x^n = x^(n//2) * x^(n//2) * x ... n是奇数
```
根据这个递归思路，就可以写出O(logn)的代码了。
```python
def normal_pow(x, n):
    if n == 0: return 0 if x == 0 else 1
    if n == 1: return x    # 递归返回条件
    
    if n & 1 == 1:
        res = normal_pow(x, n >> 1)
        return res * res * x
    else:
        res = normal_pow(x, n >> 1)
        return res * res
```

注意上面的改写一定要
```python
res = normal_pow(x, n >> 1)
return res * res
```
而不要
```python
return normal_pow(x, n >> 1) * normal_pow(x, n >> 1)
```
因为后一个，你还是调用了两次normal_pow，相当于整个递归还要整两次，这么一层层下来，效率反而可能是降低了。

还有两个提高效率的小点，判断奇偶性用与运算，以及`//2`操作用`>> 1`位运算代替。

最后，一些特殊情况别忘了考虑。因为是乘方，所以特别注意0的0次方，0的负数次方这种恶心的情况。
LeetCode上面似乎没有检查0的负数次方的case。

以上。