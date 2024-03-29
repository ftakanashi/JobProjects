## 题目描述
图像平滑器 是大小为 3 x 3 的过滤器，可以计算是周围的8个单元和它本身的值求平均灰度(即蓝色平滑器中9个单元的平均值)来应用于图像的每个单元。如果一个单元的一个或多个周围的单元不存在，我们不考虑它的平均值(即红色平滑器中的四个单元的平均值)。



给定一个代表图像灰度的 m x n 整数矩阵 img ，返回对图像的每个单元格平滑处理后的图像 。
![](https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg)

示例 1:
```
输入:img = [[1,1,1],[1,0,1],[1,1,1]]
输出:[[0, 0, 0],[0, 0, 0], [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
```
示例 2:
```
输入: img = [[100,200,100],[200,50,200],[100,200,100]]
输出: [[137,141,137],[141,138,141],[137,141,137]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
```

提示:
```
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
```

### 解法 前缀和
这题因为数据规模不大，所以按照题意直接模拟倒也是可以。
而如果使用前缀和，似乎可以更低复杂度实现。

简单来说，构造一个二维的前缀和数组，`presum[i][j]`表示原矩阵中`(0,0)`为左上角，`(i, j)`是右下角矩阵的所有值的总和。
如此，计算某个格子为中心的九宫格的所有数字的和，就可以通过`presum[i+1][j+1] - presum[i-2][j+1] - presum[i+1][j-2] + presum[i-2][j-2]`。

当然，这个过程中还需要注意这些下标是否越界，由于题意，越界可以直接将越界的拉回来，更多细节写在了代码注释中。

最后，有了九宫格的和之后，还需要求平均值，这其中还需要统计有几个有效格子，这个可以以格子为中心扫描周边八个格子检查有效性。