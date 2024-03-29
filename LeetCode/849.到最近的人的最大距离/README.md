## 题目描述
给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。

至少有一个空座位，且至少有一人已经坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

示例 1：

![](https://assets.leetcode.com/uploads/2020/09/10/distance.jpg)
```
输入：seats = [1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。
```
示例 2：
```
输入：seats = [1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
```
示例 3：
```
输入：seats = [0,1]
输出：1
```

提示：
```
2 <= seats.length <= 2 * 104
seats[i] 为 0 或 1
至少有一个 空座位
至少有一个 座位上有人
```

### 解法 模拟
题目意思不难理解，并且也很容易想到，为了能够和相邻的人距离最大，显然就应该寻找`seats`数组中，两个相邻1之间距离最大的那个地方。

于是最核心的算法框架很快就有了。
我们可以从左到右扫描一遍seats，并且记录各个1的位置，计算任意两个相邻的1之间的距离的最大值。（这里也有一点点小的贪心思想）
最终答案是这个最大值除以2。

不过这里还有一点小细节。
比如第一个元素或者最后一个元素不是1的时候，那么其实第一个1和倒数第一个1的位置两侧并没有多余的1了，
但是此时也应当计算这片距离，并且这一片距离还不用除以2。

于是，我们可以将核心的遍历范围定义为从第一个1到最后一个1。
而第一个1左边的头部以及最后一个1右侧的尾部，做特殊处理。
细节逻辑倒是不难，看代码和注释吧。