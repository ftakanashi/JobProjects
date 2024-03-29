## 题目描述
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:
```
输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```
示例 2:
```
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

### 解法 分治
虽然一看就知道可以用DFS做。
但是一开始用常规的从前往后，设计类似于`dfs(start)`之类的DFS函数，结合栈，发现并不好做。

重新思考了一下，发现可能用从前往后的DFS不如用从中间某个点分成前后两半的分治法更加好做。
当然，这两者本质上是相同的，都是递归地将复杂问题化解为更小的简单问题，并将更小简单问题的结果拼接成大问题的结果。

从分治的思想来说，对于一个输入的Expression我们可以看到，其可以被自由的组装成多个不同优先级的算式，
而判断优先级的分界点在运算符上。

即，每一个运算符都可以作为分割点将算式分成左右两块。
最简单的块当然就是一个数字的情况，而稍复杂的情况，左右两边应该都可以通过不同的优先级设计算出多个答案。
最后只要根据这个运算符的逻辑，将左右两边的多个答案做一个笛卡尔积运算即可。

举个例子，比如示例2，以第一个乘号为分割点，则可以得到左边的唯一答案`2`，而右边，根据优先级不同可以计算出
`-5, -17`，结合本符号是乘号，所以可以得到`-10`和`-34`这两个答案。
显然，左右块的计算是一个递归的过程。

如此，我们只需要遍历整个字符串，以每个符号作为分割点，就可以得到完整的所有答案了。

具体的，由于输入是一个纯字符串，我们还需要先预处理，将所有多位的数字和符号分别分割开来保存下来。
这个过程我写了一个analyze方法。
接着实现分治函数，大概长这样：`def rec(start: int, end: int) -> List[int]`。
实现后发现分治函数的输入是两个int(start和end的下标)，因此可以通过cache避免重复计算。