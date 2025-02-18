## 题目描述
给你一个二维整数数组 point ，其中 points[i] = [xi, yi] 表示二维平面内的一个点。同时给你一个整数 w 。你需要用矩形 覆盖所有 点。

每个矩形的左下角在某个点 (x1, 0) 处，且右上角在某个点 (x2, y2) 处，其中 x1 <= x2 且 y2 >= 0 ，同时对于每个矩形都 必须 满足 x2 - x1 <= w 。

如果一个点在矩形内或者在边上，我们说这个点被矩形覆盖了。

请你在确保每个点都 至少 被一个矩形覆盖的前提下，最少 需要多少个矩形。

注意：一个点可以被多个矩形覆盖。

示例 1：

![](https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-20-33-05.png)
```
输入：points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]], w = 1

输出：2

解释：

上图展示了一种可行的矩形放置方案：

一个矩形的左下角在 (1, 0) ，右上角在 (2, 8) 。
一个矩形的左下角在 (3, 0) ，右上角在 (4, 8) 。
```
示例 2：

![](https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-18-59-12.png)
```
输入：points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]], w = 2

输出：3

解释：

上图展示了一种可行的矩形放置方案：

一个矩形的左下角在 (0, 0) ，右上角在 (2, 2) 。
一个矩形的左下角在 (3, 0) ，右上角在 (5, 5) 。
一个矩形的左下角在 (6, 0) ，右上角在 (6, 6) 。
```
示例 3：

![](https://assets.leetcode.com/uploads/2024/03/04/screenshot-from-2024-03-04-20-24-03.png)
```
输入：points = [[2,3],[1,2]], w = 0

输出：2

解释：

上图展示了一种可行的矩形放置方案：
一个矩形的左下角在 (1, 0) ，右上角在 (1, 2) 。
一个矩形的左下角在 (2, 0) ，右上角在 (2, 3) 。
```

提示：
```
1 <= points.length <= 105
points[i].length == 2
0 <= xi == points[i][0] <= 109
0 <= yi == points[i][1] <= 109
0 <= w <= 109
所有点坐标 (xi, yi) 互不相同。
```

### 解法 排序
由于矩形的高度不管定多高都行，没有任何成本，所以我们只需要关注点的横坐标即可。
又因为矩形的横向跨度只需要小于等于w即可， 所以本着贪心的原则，为了让总的矩形数目最小，应该尽量让矩形的宽度达到`w`。

于是一个很自然的解法就出来了。
我们将所有点按照横坐标进行排序。然后从左到右扫描。

第一个点开始，我们就以这个点的坐标为横坐标构建第一个矩形。记录下矩形的右端点。
之后遍历过程中，如果点还在当前矩形范围内，就不做任何事，否则就以当前点的坐标构建一个新矩形。