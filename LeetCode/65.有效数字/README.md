## 题目描述
验证给定的字符串是否可以解释为十进制数字。

例如:
```text
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false
```

说明: 我们有意将问题陈述地比较模糊。

在实现代码之前，你应当事先思考所有可能的情况。

这里给出一份可能存在于有效十进制数字中的字符列表：
- 数字 0-9
- 10的指数 - "e"
- 正/负号 - "+"/"-"
- 小数点 - "."

当然，在输入中，这些字符的上下文也很重要。

### 解法1 简单的分类讨论
最简单朴素的一种办法，就是if/else简单讨论。

当然，合理地设计分支路线间的逻辑关系可以简化讨论的可能性。

比如，显然对于所有非1234567890+-.eE的字符，如果扫描到了直接可以返回False。

然后第一个应该被讨论的是e和E，因为他可以将字符串分成base和10的次幂两部分。

而每一部分的判别，其实是互相独立的。这个判别函数也可以拿出来用来判断，字符串s中本身就没有e的整体合法情况。

代码里写了注释。

### 解法2 有限状态机
解法1虽然能过，但是代码不优雅。

有限状态机DFA在这题里也能做。
>参考https://leetcode-cn.com/problems/valid-number/solution/biao-qu-dong-fa-by-user8973/
>
>![](https://pic.leetcode-cn.com/0683d701f2948a2bd8c235867c21a3aed5977691f129ecf34d681d43d57e339c-DFA.jpg)
>
>另一个：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/