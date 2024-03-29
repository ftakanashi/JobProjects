## 题目描述
我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。

![](https://assets.leetcode.com/uploads/2019/07/28/azboard.png)

我们可以按下面的指令规则行动：
```
如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）
```

返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。

示例 1：
```
输入：target = "leet"
输出："DDR!UURRR!!DDD!"
```
示例 2：
```
输入：target = "code"
输出："RR!DDRR!UUL!R!"
```

提示：
```
1 <= target.length <= 100
target 仅含有小写英文字母。
```

### 解法 哈希表
这题乍一看以为要用BFS之类的探索方法来做呢。
其实仔细审题，发现题目中的每个测试用例，其字母板都是固定的。
因此每两个字母之间的最短路径也总是固定的，不需要探索。

于是思路就出来了，通过一个哈希表先保存每个字母的横纵坐标，然后将两个坐标的差求出来，就可以求得两个字母之间最短的一个路径了。

看似到这里就完事了。但是还有一些特殊情况需要考虑，就是字母`z`。

比如从字母v走到z，此时如果按照我们的坐标差的思路来做，那么显然最短路径有两种，分别是线向下再向左，或者是先向左再向下。
可以看到，前者的这条路径是不行的，中间有虚空。

好在整个棋盘上只有z这一个字母是特殊的。并且走到z的入口总是u。
所以在进行路径生成前，我们先判断是否终点是z，若是，则将目标先改为u，最后再手工加上一个向下的步骤即可。

但是这样还没有完事。
还有一个更更特殊的情况，就是起始和终点都是z，此时没必要绕一下u。
这个可以通过在最开始就加一条判断，若起点和终点是同一个，则不用生成路径直接收割即可。

最终看代码。