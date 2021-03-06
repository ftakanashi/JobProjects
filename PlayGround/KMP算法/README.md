# KMP算法

## 前情提要
KMP算法的适用问题，是字符串匹配。即python中的`t.find(p)`方法的功能。

这里，`t`成为目标串target，`p`称为模式串pattern。假设两者长度各自为`n`和`m`且`n >= m`，有：
```text
t_0 t_1 t_2 ... t_{n-1}
p_0 p_1 ... p_{m-1}
```

此时最一般的算法是线性扫描。是双层循环的。
外层依次扫描t串，确定一个待比较的子串的开始点，
内层则依次扫描比对t的这个子串 和 p是否相同。

这样的做法可以做如下优化：
比如t和p是下面这样的：
```text
abbbabc...
abbbc
```

注意，此时第一次比对在p是c处失败了。
按照线性扫描的做法，接下来要比对的是如下情况：
```text
abbbabc...
 abbbc
```
但是，其实在第一次比对中由于p是在c处失败，换言之，p在c处之前的子串"abbb"是匹配成功了的。
此时往后走一格显然很没有必要，因为a和b肯定是对不上的。事实上走两格，走三格都没有必要。

完全可以，直接比对这种情况：
```text
abbbabc...
    abbbc
```

也就是说，线性扫描不必一格一格走，而可以"跳跃着"扫描。从而大大提高扫描的效率。

## KMP算法本体
KMP算法的关键在于，跳跃着走时，一次可以跳几步。

根据上面的分析，其实可以跳几步，和在p的哪个位置匹配失败了有关，而跟t串是什么样的其实没有关系。

因此，可以事先扫描p串，得到一个pnext数组。数组的每个值代表 对应位置匹配失败时可以跳的步数。

从结论来说，**`pnext[i]`的值`k`的意义是，`p_0 p_1 ... p_{i-1}`这个p的子串中，最长的共同前后缀的长度。**

也就是说`p_0 ... p_{k-1} p_k ... p_{i-k} ... p_{i-1}`中，

前缀`p_0 ... p_{k-1}`和后缀`p_{i-k} ... p_{i-1}`完全一致。

**另外为了实现上的方便，定义`pnext[0]`一定是`-1`**

比如`abbcabd`这个p串的pnext，是这样的：
```text
[-1, 0, 0, 0, 0, 1, 2]
```

注意最后两个值。倒数第二个，本身字符是b，但是本身不算，所以看`abbca`的最长共同前后缀。
由于前缀`a`和后缀`a`一致，所以值是1。

另一方面，最后一个位置，他看的是他之前的`abbcab`，前后缀`ab`一致，所以是2。

这个pnext通过如下函数可以获得：
```python
def generate_pnext(s: str) -> List[int]:
    i, k, m = 0, -1, len(s)
    pnext = [-1 for _ in range(m)]
    while i < m-1:
        if k == -1 or s[i] == s[k]:
            pnext[i + 1] = k + 1
            i += 1
            k += 1
        else:
            k = pnext[k]

    return pnext
```

得到了pnext之后，只要设置双指针，按线性扫描的开场那样开始扫描t和p。

而当遇到匹配失败的情况，根据pnext的信息往前跳跃即可。kmp本体函数如下：
```python
def kmp(t, p):
    pnext = generate_pnext(p)
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            i += 1
            j += 1
        else:
            i = pnext[i]
    if i == m: return j - i
    return -1
```

两个函数在代码模式上还有点像，所以可以一起记忆。