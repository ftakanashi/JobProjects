## 题目描述
给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。

给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。

返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。

示例 1:

![](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)
```
输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 树如图所示。
我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
```
示例 2:
```
输入: n = 1, edges = []
输出: [0]
```
示例 3:
```
输入: n = 2, edges = [[1,0]]
输出: [1,1]
```

提示:
```
1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
给定的输入保证为有效的树
```

### 解法 树形DP
一种新套路，又是疯狂抄答案翻译答案的一天…

题意不难读懂，我们先从简单的问题入手。
如果只需要求根节点到所有其他节点的距离总和，应该怎么做呢？
显然可以通过一个dfs来做。具体的，我们可以为每个节点维护一个DP值表示其到其所有后辈节点之间的距离总和。
对于叶子节点来说这个值是0。
对于非叶子节点来说，这个值应该这样计算：
```python
dp[node] = 0
for nxt in node.children:
    dp[node] += sum(dp[nxt] + size(nxt))
```
注意：这题的树并不是二叉树，所以不能简单地`node.left`和`node.right`。

其中`size`表示的是一棵树的总节点数量。这部分信息其实也可以在一次dfs中获取出来，我们用一个`sz`数组来维护。

这么一来，第一个DFS过程其实就已经明确了。如下：
```python
# 构建图
graph = defaultdict(set)
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

# 构建DP数组和SZ数组
dp = [0 for _ in range(n)]
sz = [1 for _ in range(n)]
def dfs(node, parent):
    for nxt in graph[node]:
        if nxt == parent: continue
        dfs(nxt, node)
        dp[node] += dp[nxt] + sz[nxt]
        sz[node] += sz[nxt]
```
这题中虽然给出的结构是树，但是并没有给出树节点的定义，根据官答和很多人的实践，最终还是采用了普通的图来构建结构。
这就要注意在遍历的时候要避免遍历当前节点的父节点，以避免死循环。

显然，执行一次`dfs(0, None)`之后，`dp[0]`的值就是根节点的正确答案，即从根节点出发到所有子节点的距离总和了。

可是至此，题目没有做完。除了根节点之外，其他节点该怎么办呢？
一个比较直接的方法是，我是不是可以从每个节点出发都完成一次上述过程。

这里一个隐含的条件是，这题给的结构是一个一般意义上的树。意味着每条边都是无向的边。
这也意味着每个节点都是可以作为根节点的。

比如示例1中虽然给出的中是0是根节点，上面`dfs(0, None)`的也是0对应的答案。
但是如果将2作为根节点，也是完全可行的，此时`dfs(2, None)`，就是答案。当然此时的dp值和sz值就有变化了。
这其实就是树形DP的精髓，换根。

以0和2互相换根为例。换根后，`sz[0]`和`sz[2]`的变化比较简单。
```
sz[0] -= sz[2]
sz[2] += sz[0]
```
注意这两句一定得先后执行，因为下边的 `+= sz[0]`的值是上面减过之后的值。

同理，对于DP值，`dp[0]`由于0不再是根节点，需要去除原先2作为0的子节点时带来的dp值贡献，这部分具体为`dp[2] + sz[2]`。
对于2来说也同理要加上新的0作为子节点带来的贡献。总的就是
```python
dp[0] -= dp[2] + sz[2]
dp[2] += dp[0] + sz[0]
```

于是，基于第一次DFS完成后的dp和sz的情况，我们可以立刻进行第二次DFS。这次我们尝试将树中所有父子节点都挨个进行一次换根尝试，从而计算出
原子节点作为根节点时的DP值，从而计算出所有节点的最终答案。

更多细节看代码。