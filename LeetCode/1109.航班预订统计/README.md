## 题目描述
这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

示例 1：
```
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
```
示例 2：
```
输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]
```

提示：
```
1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104
```

### 解法 差分数组 前缀和
一道典型的用差分数组就可以做的题目。

复习一下差分数组的概念，就是给定一些`[s, e, v]`三元组，`s,e`表示了一个数组上的范围而`v`代表了要在这个范围上加的一个值。

现在要求的是在经历若干个三元组之后每个点上值的总和。
构建差分数组`diff`（长度为n+1），对于每个三元组，`diff[s] += v`，`diff[e+1] -= v`。

然后对diff数组求前缀和，得到的前缀和数组就是要求的答案了。

这题题设和上面说的一模一样，就不多说了。直接看代码。
类似的题目还可以看`LC.1094`