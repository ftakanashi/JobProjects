## 题目描述
共有 k 位工人计划将 n 个箱子从旧仓库移动到新仓库。给你两个整数 n 和 k，以及一个二维整数数组 time ，数组的大小为 k x 4 ，其中 time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi] 。

一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 k 位工人都在桥的左侧等待。为了移动这些箱子，第 i 位工人（下标从 0 开始）可以：
```
从左岸（新仓库）跨过桥到右岸（旧仓库），用时 leftToRighti 分钟。
从旧仓库选择一个箱子，并返回到桥边，用时 pickOldi 分钟。不同工人可以同时搬起所选的箱子。
从右岸（旧仓库）跨过桥到左岸（新仓库），用时 rightToLefti 分钟。
将箱子放入新仓库，并返回到桥边，用时 putNewi 分钟。不同工人可以同时放下所选的箱子。
```

如果满足下面任一条件，则认为工人 i 的 效率低于 工人 j ：
```
leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj 且 i > j
```

工人通过桥时需要遵循以下规则：

如果工人 x 到达桥边时，工人 y 正在过桥，那么工人 x 需要在桥边等待。
如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 效率最低 的工人会先过桥。
如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。如果同时有多个工人在左边等待，那么 效率最低 的工人会先过桥。
所有 n 个盒子都需要放入新仓库，请你返回最后一个搬运箱子的工人 到达河左岸 的时间。

示例 1：
```
输入：n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
输出：6
解释：
从 0 到 1 ：工人 2 从左岸过桥到达右岸。
从 1 到 2 ：工人 2 从旧仓库搬起一个箱子。
从 2 到 6 ：工人 2 从右岸过桥到达左岸。
从 6 到 7 ：工人 2 将箱子放入新仓库。
整个过程在 7 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 6 。
```
示例 2：
```
输入：n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
输出：50
解释：
从 0 到 10 ：工人 1 从左岸过桥到达右岸。
从 10 到 20 ：工人 1 从旧仓库搬起一个箱子。
从 10 到 11 ：工人 0 从左岸过桥到达右岸。
从 11 到 20 ：工人 0 从旧仓库搬起一个箱子。
从 20 到 30 ：工人 1 从右岸过桥到达左岸。
从 30 到 40 ：工人 1 将箱子放入新仓库。
从 30 到 31 ：工人 0 从右岸过桥到达左岸。
从 31 到 39 ：工人 0 将箱子放入新仓库。
从 39 到 40 ：工人 0 从左岸过桥到达右岸。
从 40 到 49 ：工人 0 从旧仓库搬起一个箱子。
从 49 到 50 ：工人 0 从右岸过桥到达左岸。
从 50 到 58 ：工人 0 将箱子放入新仓库。
整个过程在 58 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 50 。
```

提示：
```
1 <= n, k <= 104
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000
```

### 解法 模拟 堆
算得上是相当复杂的模拟题了……

首先是读懂题意。
需要大致把握一个感觉，就是整个流程并没有像小学奥数题里的统筹安排那样复杂，整体还是相对比较线性的。
但是在线性中，唯独又有一个拿放箱子的过程是可以并行的。

对于这个复杂问题，我们将其分解成一个个简单的问题逐个来思考。

首先考虑桥左边或者右边有一些工人需要过桥时的情况。
首先右边优先级应当高于左边。因为在桥右边等待过桥的人手上必然有箱子，所以优先将其走到左边放箱子没毛病。
然后针对一批要过桥的人，题目也给出了优先度的定义，就是效率，而且是效率越低越优先。显然这里可以用堆来维护要过桥的人。
结合实际的`heapq`的用法，这里我们定义一个优先级的函数为
```python
f = lambda i: (-(time[i][0] + time[i][2]), -i)
```
注意这里的第二项是`-i`，因为在左右过桥时间总和相等情况下按照题意下标越大的效率越低，也就越优先，因此要加负号。

接着， 一个比较难想到的点，是对正在工作的人进行堆的维护。
比如在右边旧仓库中拿箱子的一些人，将他们拿到箱子的预计时间按小顶堆进行维护。
这是因为拿放箱子和过桥这两种行为之间可能存在重叠，所以我们无法用一条数轴单向地递增维护已经用掉的时间。
由于过桥时间总是实打实的，而拿放箱子可能存在并行，所以我们以过桥时间作为基准进行已经使用的时间的递增维护。
而在一个人过桥，把时间加上一点之后，可能此时在仓库中拿放箱子的一些人已经完成了工作。
此时就应该按照完成预计时间从小到大地依次将这部分人从工作队列中拿出并充入过桥等待队列。

然后是总体的判断框架的设计，这里也直接照抄官答了…
接下来就按照实际的算法来说明，这样更加方便一些。

按照上面的叙述，首先初始化四个堆，`wait_l, wait_r, work_l, work_r`分别表示在桥左右两边等待过桥的人的队列，以及在桥左右两边仓库里正在
放拿箱子的人的队列。
然后初始化 `curr = 0` 表示已经流逝的时间。

维护一个 `remain` 值表示在旧仓库中箱子的数量。
只要 `remain > 0` 说明还有箱子没从旧仓库中搬完，所以就要进入循环。
同样的，由于题目要求所有人最终都到桥左边，所以`wait_r`或者`work_r`中还有人时也都要继续循环。
所以总的循环入口条件是 `while remain > 0 or wait_r or work_r`。

进入循环后考虑各个队列是否有人的各种情况来执行对应的操作。这里设计可以相对自由一点，官答是这样设计的。

情况1.
如果`wait_r`有人，优先让堆顶的人过桥，显然过桥后此人进入`work_l`队列。
同时 `curr` 应该加上这人过桥的时间。

情况2.
若`wait_r`没人，则考虑是否`remain > 0`且`wait_l`有人。若是说明可以让一个人从左边过桥拿箱子。
和上一中情况类似，过桥后此人进入 `work_r` 队列，并且 `curr` 加上相应的时间。
不同的是，此时旧仓库少了一个箱子，因此 `remain -= 1`。

情况3.
其余情况。此时`wait_l`和`wait_r`都没有人，说明所有人都在工作，没人需要过桥。
此时由于拿放箱子是可以并行的，因此直接取出 `work_l` 和 `work_r` 中堆顶的人，看两遍预计完成时间是否大于`curr`。
若是，则将时间推进到那个值。若否，其实可以将这部分人从`work`队列中拿出来。
不过后一种情况我们统一在最后做。

以上情况考虑完之后，就考虑统一扫描两个 `work` 队列。因为经过上面处理后，可能 `curr` 被向前推进了不少（有人过桥）。
而此时 `work` 队列中可能很多人都已经完成了拿放箱子的工作。
此时可以将这部分人全部pop出来，放到 `wait` 队列中。

按照以上复杂逻辑一行行码代码就行了。具体的代码里我也会加上一些注释。

只能说，这是一个相当复杂的模拟题…