## 题目描述
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: `[0,1]`

给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例 1:
```
输入: 2, [[1,0]] 
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
```
示例 2:
```
输入: 4, [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
     因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
```
说明:
1. 输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
2. 你可以假定输入的先决条件中没有重复的边。

提示:
1. 这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
2. 通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
3. 拓扑排序也可以通过 BFS 完成。

### 审题
出现了，一个新套路。拓扑排序。

拓扑排序的概念是指，针对一个有向图中的所有节点。给出一种节点的排列顺序，使得其满足
针对任何一条边`a -> b`都有，排序序列中`a`在`b`的前面。

拓扑排序有两个明显的特点。

第一，不唯一。极端点来说，一个图没有任何边，那么任意一个节点的排列都是符合要求的拓扑排序。

第二，不一定存在。当图中含有环时（注意是有向图，因此环指的是一个循环结构），比如`a`和`b`之间互相指向对方，
那么无论在最终的序列里如何安排他们俩的前后关系，都有一条边不符合要求。

说到这里，其实这道题就很明显了。他就是给出一个图求一个拓扑排序序列的问题。

### 解法 DFS
利用DFS求拓扑排序的思想如下。同时这也是一个求有向图里有没有环的算法。

在DFS遍历的过程中，对于任意一个节点，我们认为其有三种状态。
第一，未被遍历。第二，被遍历但未完成。第三，被遍历且完成。

具体遍历过程中，如果从节点`a`出发遍历其下游节点。首先将`a`本身从第一个状态置为第二个状态。
如果某个下游节点`b`处于第一种状态，显然递归进行下一层DFS。
如果某个下游节点`b`处于第三种状态，那么不需要对其进行递归，因此跳过。
如果某个下游节点`b`处于第二种状态，说明图里有环，此时可以直接向上层报告，结束递归。

完成对所有下游节点的遍历之后，将`a`从第二种状态置为第三种状态，收割结果，结束函数。为了区别这种结束和上述讨论的提前结束递归的返回的区别，
设计DFS函数返回一个bool值。

最后，在外层调用DFS的时候，入口节点应该处于第一种状态。此外，若某次DFS返回了False，说明此次遍历时发现了图中的环，因此可以直接返回空列表，即
不存在拓扑排序。

注意，使用一个列表收割结果时，因为这是一个DFS操作，所以某种意义上这个列表其实是个栈（最先被收割的其实是最底层的节点）。
因此最终返回时记得要把结果列表给逆序一下。