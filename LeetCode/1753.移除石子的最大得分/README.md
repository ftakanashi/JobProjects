## 题目描述
你正在玩一个单人游戏，面前放置着大小分别为 a​​​​​​、b 和 c​​​​​​ 的 三堆 石子。

每回合你都要从两个 不同的非空堆 中取出一颗石子，并在得分上加 1 分。当存在 两个或更多 的空堆时，游戏停止。

给你三个整数 a 、b 和 c ，返回可以得到的 最大分数 。

示例 1：
```
输入：a = 2, b = 4, c = 6
输出：6
解释：石子起始状态是 (2, 4, 6) ，最优的一组操作是：
- 从第一和第三堆取，石子状态现在是 (1, 4, 5)
- 从第一和第三堆取，石子状态现在是 (0, 4, 4)
- 从第二和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：6 分 。
```
示例 2：
```
输入：a = 4, b = 4, c = 6
输出：7
解释：石子起始状态是 (4, 4, 6) ，最优的一组操作是：
- 从第一和第二堆取，石子状态现在是 (3, 3, 6)
- 从第一和第三堆取，石子状态现在是 (2, 3, 5)
- 从第一和第三堆取，石子状态现在是 (1, 3, 4)
- 从第一和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：7 分 。
```
示例 3：
```
输入：a = 1, b = 8, c = 8
输出：8
解释：最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。
```

提示：
```
1 <= a, b, c <= 105
```

### 解法 数学
这题有比较机械的贪心解法。具体的贪心策略是，总是从石头数量最多的两堆石头中取，这样计算最终得分，也可以得到正确答案。
但是问题在于这样一次一次减，效率很低。

这里提出一种可以通过数学规律O(1)时间完成的思路。
关键在于关注a, b, c中较小的两个数的和与较大数之间的大小关系。

我们不妨设`a <= b <= c`。这样就是比对`a + b`和`c`之间的关系。

显然，当`a + b <= c`的时候，不论什么时候，同时从`a`和`b`中取石子是不明智的。与其ab间内卷，不如拉c下水。
也就是说每一次操作都是从a或者b中拿一个石头，c中拿一个石头。这样最后ab都拿完，c还是有余量。
显然此时答案会是`a + b`。

另一方面，如果`a + b > c`，此时第一阶段仍然保持和上面同样的策略，但是我们尽可能保证a和b之间数量差的不是太多。
可以证明，当c被取完的时候，a和b的石头数量相等或者差1（别忘了c是最大数且`a + b > c`这两个条件）
接下来可以继续把a和b取完。

上述过程写代码好像还是有点麻烦，我们辅助一些数学推导。
设在c被取完时，ac组合和bc组合各贡献了`k1`和`k2`分。显然`k1 + k2 = c`。
接下来我们总结一下，答案是：
`(k1 + k2) + floor( ((a - k1) + (b - k2)) /  2 )`。
将这个式子化简后其实就是`floor((a + b + c) / 2）`，即`(a + b + c) // 2`。

有了上面的数学工作，代码就好写多了。具体看代码吧。
