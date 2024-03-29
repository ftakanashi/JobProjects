## 题目描述
你正在经营一座摩天轮，该摩天轮共有 4 个座舱 ，每个座舱 最多可以容纳 4 位游客 。你可以 逆时针 轮转座舱，但每次轮转都需要支付一定的运行成本 runningCost 。摩天轮每次轮转都恰好转动 1 / 4 周。

给你一个长度为 n 的数组 customers ， customers[i] 是在第 i 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 i 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 boardingCost ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。

你可以随时停下摩天轮，即便是 在服务所有游客之前 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，将免费进行所有后续轮转 。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 下一次轮转 。

返回最大化利润所需执行的 最小轮转次数 。 如果不存在利润为正的方案，则返回 -1 。

示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/wheeldiagram12.pnghttps://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/wheeldiagram12.png)
```
输入：customers = [8,3], boardingCost = 5, runningCost = 6
输出：3
解释：座舱上标注的数字是该座舱的当前游客数。
1. 8 位游客抵达，4 位登舱，4 位等待下一舱，摩天轮轮转。当前利润为 4 * $5 - 1 * $6 = $14 。
2. 3 位游客抵达，4 位在等待的游客登舱，其他 3 位等待，摩天轮轮转。当前利润为 8 * $5 - 2 * $6 = $28 。
3. 最后 3 位游客登舱，摩天轮轮转。当前利润为 11 * $5 - 3 * $6 = $37 。
轮转 3 次得到最大利润，最大利润为 $37 。
```
示例 2：
```
输入：customers = [10,9,6], boardingCost = 6, runningCost = 4
输出：7
解释：
1. 10 位游客抵达，4 位登舱，6 位等待下一舱，摩天轮轮转。当前利润为 4 * $6 - 1 * $4 = $20 。
2. 9 位游客抵达，4 位登舱，11 位等待（2 位是先前就在等待的，9 位新加入等待的），摩天轮轮转。当前利润为 8 * $6 - 2 * $4 = $40 。
3. 最后 6 位游客抵达，4 位登舱，13 位等待，摩天轮轮转。当前利润为 12 * $6 - 3 * $4 = $60 。
4. 4 位登舱，9 位等待，摩天轮轮转。当前利润为 * $6 - 4 * $4 = $80 。
5. 4 位登舱，5 位等待，摩天轮轮转。当前利润为 20 * $6 - 5 * $4 = $100 。
6. 4 位登舱，1 位等待，摩天轮轮转。当前利润为 24 * $6 - 6 * $4 = $120 。
7. 1 位登舱，摩天轮轮转。当前利润为 25 * $6 - 7 * $4 = $122 。
轮转 7 次得到最大利润，最大利润为$122 。
```
示例 3：
```
输入：customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92
输出：-1
解释：
1. 3 位游客抵达，3 位登舱，0 位等待，摩天轮轮转。当前利润为 3 * $1 - 1 * $92 = -$89 。
2. 4 位游客抵达，4 位登舱，0 位等待，摩天轮轮转。当前利润为 is 7 * $1 - 2 * $92 = -$177 。
3. 0 位游客抵达，0 位登舱，0 位等待，摩天轮轮转。当前利润为 7 * $1 - 3 * $92 = -$269 。
4. 5 位游客抵达，4 位登舱，1 位等待，摩天轮轮转。当前利润为 12 * $1 - 4 * $92 = -$356 。
5. 1 位游客抵达，2 位登舱，0 位等待，摩天轮轮转。当前利润为 13 * $1 - 5 * $92 = -$447 。
利润永不为正，所以返回 -1 。
```

提示：
```
n == customers.length
1 <= n <= 105
0 <= customers[i] <= 50
1 <= boardingCost, runningCost <= 100
```

### 解法 模拟
这题不难，读懂题意然后按照规则模拟即可。

不难注意到，由于来的客人并不区分彼此（比如可以不同的几波人坐同一个摩天轮），因此人数只是一个数字。
我们可以用一个变量`queue`表示当前正在排队的人数。

每转动一次摩天轮，如果`queue`大于4，则坐满4人，否则就清空`queue`即可。

另外，还需要注意题目的一个比较难注意到的条件，就是`customers`数组中每个数字不论是多少，都至少对应了一次摩天轮转动。
比如test case中有一个是`[5,0,0,0,0,30]`。中间有很多零，但是不能直接不转摩天轮以节省成本。。
换言之，即便明知道这样转是亏本的，但是还是得转（在天上那些人还得下来不是…）

另外还需要注意，并不是遍历完customers就行了，别忘了遍历完之后，可能`queue`还不为零，也就是说还有游客在排队等待上摩天轮。
因此遍历完customers之后还应该有个`while queue > 0`的循环处理剩下的人。

总的来说，思路是这样的：
首先遍历customer，记录转动的次数以及每次转动之后当前累计的利润值。并实时更新当前正在排队的人数。
当当前累计利润值大于记录的最大利润值时就记录一下当前转动的次数作为候选答案。
遍历完customer之后，考虑到可能queue仍然大于0，所以需要第二轮`while queue > 0`的遍历。遍历内部的逻辑和上面类似，
只要转动、更新利润、记录答案、更新排队人数，就可以了。