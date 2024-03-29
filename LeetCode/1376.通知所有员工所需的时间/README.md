## 题目描述
公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。

在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。题目保证从属关系可以用树结构显示。

公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。

第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。

返回通知所有员工这一紧急消息所需要的 分钟数 。

示例 1：
```
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司总负责人是该公司的唯一一名员工。
```
示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/graph.png)
```
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
输出：1
解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。
```

提示：
```
1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
如果员工 i 没有下属，informTime[i] == 0 。
题目 保证 所有员工都可以收到通知。
```

### 解法 BFS
题目不难理解，理解之后就知道这是一道简单的探索的题目了。
探索的话自然就是要不DFS要不BFS。我们这边采用BFS的做法。

首先虽然是一个树结构，但是题目没有给出树节点的类之类的，所以合理还是首先需要构建图。
然后BFS的过程中，扫描到一个员工的时候，可以考虑将通知发送到这个人时已经耗费的总时间也维护起来。
这样最终只要返回整个探索过程中，全局的一个总耗时的最大值作为答案即可。
显然，在这样一个框架下，BFS的起始值是`(headId, 0)`。

探索过程中，若某个节点有后续节点，则将`(next, time + informTime[node])`入队即可。

由于树是单向的结构，因此不需要考虑陷入死循环的情况。