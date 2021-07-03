# 概述
## 什么是并查集
并查集解决的问题，是无向图的问题。

具体来说，当某个图确定时，构建并查集可以分析图中所有节点之间的关系。

构建完成后的并查集可以通过O(1)的时间和O(n)的空间，来找出图中每个联通分量。

以`LC 547.朋友圈`的场景来举例说明。

当我们有一群人，A是B的朋友，B是C的朋友，那么就认为A也是C的朋友。此时
`A-B-C`形成一个朋友圈。

如果此时，还有`D-E`两个人互为朋友，但是D，E任意一个都不与A，B，C中任意一个是朋友。

所以此时存在两个朋友圈，用图来解释就是：
```text
A-B-C
D-E
```
存在两个联通分量，所以就是两个朋友圈。

当给定你一些输入，比如像547题一样用一个矩阵表示各个节点之间边的关系，让你求出其中"朋友圈"个数，
即联通分量个数，这种情况就可以使用并查集。

## 并查集算法描述
具体如何想到并查集这样一种算法就不说了。总之就当他是既成事实，接受了就好。

我们使用一个长度为节点个数n的数组来实时维护各个节点处于哪个联通分量中，并扫描图。

这里有一个问题，"处于哪个联通分量中"该如何表示。或者说"连通分量"该如何表示。
最先容易想到的是用一个set来表示。但是一来set本身要空间比较大，二来后续会讲到的一些操作中，set并不是很方便。

前人研究出的办法是，用树来表示联通分量，并且在上述数组中存放各个联通分量的父节点。
>这里并没有实际实现树结构，而只是逻辑中有树并且用数组维护了父子节点之间的关系。
>
>和堆的思想类似

接下来，当我们发现`x`和`y`节点之间有连接时，根据数组**查找**到`x`节点所属联通分量的父节点，
而父节点可以进一步回溯，迭代地找到这个联通分量的根节点`root_x`。

同理，根据`y`节点也可以查找到所属联通分量的根节点`root_y`。

如果`root_x`和`root_y`相同，显然两者已经处于同一连通分量中了，不必做任何操作。
如果两者不同，那么就将其中一个联通分量中的根节点指向另一个根节点，完成树的**合并**操作。

如此，先查找，再合并，随着图的扫描，不断地减少连通分量个数，直至扫描结束。

也是因为查找+合并的策略，这算法被称为，并查集。

# 实现

初始化状态下，我们假设图中没有任何连接着的边，此时联通分量个数显然就和节点个数相当。
此时这个数组是类似于`fa = [i for i in range(n)]`。即每个联通分量的根节点都是节点自己。`

实现并查集的本质是实现这样一个接口：
```python
class UnionFindSet:
    __init__(self, n: int)
    find(self, x: int) -> int
    union(self, x: int, y: int)
```

`find`方法接收一个合法的下标`x`，并迭代地寻找根节点，返回根节点的下标。

`union`方法接收两个合法下标`x, y`，将找到他们各自所属联通分量的根节点，并且进行根节点之间的合并。

于是第一版代码就有了：
```python
class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
    
    def find(self, x):
        while x != self.fa[x]:    # 当某个位置下标的值就是下标自己，说明其是联通分量的根节点
            x = self.fa[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # 此时self.fa[root_x] == root_x，因为root_x是这个联通分量的根节点
            # 然后，将父节点重置为root_y，相当于将两个连通分量合并
            # 合并后的分量，根节点是原root_y
            self.fa[root_y] = root_x
```

## 路径压缩优化
上述算法有一个问题，当图本身退化成一个链表的时候，`find`方法每次都要O(n)时间。

事实上可以想见，使用`find`回溯寻找根节点的过程，存在大量重复的计算。

所以，可以考虑改变`fa`中值的定义，
不是保存每个节点的父节点，
而是直接保存每个节点的根节点。因为我们也只关心某个节点和跟节点之间的关系，
所以中间那些父节点是什么，这部分信息完全删掉也没事。

但是这样修改之后，union时不能简单地`self.fa[root_x] = root_y`了。事实上`x`所属联通分量中，所有节点都要做这个改变。
如果直接在union中加代码，会显得比较困难。因为要从根节点开始从上向下搜索。

解决办法是，将这个过程在find中实现。

find改造如下：
```python
def find(self, x):
    r = x
    while r != self.fa[r]:
        r = self.fa[r]
    # 此时r是x节点所属连通分量的根节点
    while x != r:
        # 向上搜索root的过程中，途径所有节点的值都换成r
        tmp = self.fa[x]
        self.fa[x] = r
        x = tmp
    return r
```

如此，在每一次union过后，虽然被union的分量中各个节点的根节点信息还不会被实时更新。
但是只要这些节点后续被`find`，那么就可以保证最新信息被更新上去。

## 递归式find优化
以上路径优化的过程，其实可以轻松用递归的方式实现。
虽然本质上迭代和递归是一样的，但是递归式的表达更容易记忆。
```python
def find(self, x):
    if self.fa[x] != x:
        self.fa[x] = self.find(self.fa[x])
    return self.fa[x]
```

所以并查集写成这样：
```python
class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
    
    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_y] = root_x
```

## 基于哈希表（字典）的实现
以上实现的并查集，其核心还是一个顺序表。
因此功能会受到下标（必须是数字形式）的限制，以及动态扩展比较麻烦。
解决上述两个问题，可以采用基于字典的实现。

和基于数组的实现不同的地方在于，在find方法中要对x还没有出现在字典中的情况进行处理。

```python
class UnionFind:
    def __init__(self):
        self.fa = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_y] = root_x
```

## 加入rank优化
以上所有实现中的union方法，其实有个比较令人恶心的点。
无脑地另y的根节点和x一致即`self.fa[root_y] = root_x`。
那为什么不能反过来呢。

换句话说，如果x所在的连通分量很小很浅，而y所在的分量很大很深，此时如果无脑将y的根节点置成和x一致，那y所在分量所有节点都要改。
显然不太合理。

如果能在更换根节点前，得知两个分量各自的深度就好了，此时就可以考虑加入rank数组维护这部分信息。
（这里深度的定义是从根节点开始可以遍历到最远的同一个树中的节点，连接到那个节点所需要的边数）

显然最开始rank初始化是0，表示单节点图。union的时候，选择深度较大的根节点作为基准，把深度小的树的根节点指向它。

如果两树深度相同，原则上可以随便连，这里采用把y连到x，这样的话x的深度要+1。

这种加入rank的优化叫Union by rank，实现如下：

```python
class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0    # 初始化
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:    # 这里加上判断
                self.fa[root_x] = root_y    # x的rank至少比y的rank-1小，因此即使合并过去self.rank[root_y]不会变
            else:
                self.fa[root_y] = root_x
                # 别忘了相等时及时加深度
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1
```

## 一种可以实时统计每个分量节点数目的变体
用并查集解决的问题，大多都不会是建立完并查集就完事了。

往往需要我们进一步地考察并查集的性质并得到结果。有时候为了方便，可以考虑修改并查集本体代码，埋入某些功能。
这样最终要求的某些性质，在并查集建立过程中就动态维护了起来，最终只要取出来即可。

比如我想知道某个连通分量最终有几个节点。此时可以考虑在并查集中加上size这个属性，实时维护各个分量的节点数目。
```python
class UnionFind:
    def __init__(self):
        self.fa = {}
        self.rank = {}
        self.size = {}

    def find(self, x):
        if x not in self.fa:
            self.fa[x] = x
            self.rank[x] = 0
            self.size[x] = 1    # 初始化
        elif self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.fa[root_x] = root_y
                self.size[root_y] += self.size[root_x]    # 实时维护分量节点数量
            else:
                self.fa[root_y] = root_x
                self.size[root_x] += self.size[root_y]    # 实时维护分量节点数量
                if self.rank[root_x] == self.rank[root_y]: self.rank[root_x] += 1
```

和上述代码类似的，很多这种利用并查集求一些比较拐弯抹角的结果时，都可以这么稍微修改下并查集本体代码来达到目的。

修改的时候注意考虑find和union的时候分别发生甚么变化，该如何实时维护即可。

# 分析和其他
理想情况下，当并查集构建完成并被`find`够一定次数后，可以认为所有的信息都被更新了。
此时再根据下标查找连通分量时就只需要O(1)时间。
在并查集还没把信息更新透每次union和find操作都是O(logn)的。

空间方面，显然全程只用了O(n)的数组。

以上说明的并查集，前提都是在开始扫描前n的值是固定的，即节点数量不变。
如果节点数量可变，比如朋友圈问题中，新加入一个人，并给出其与其他人的朋友关系，问朋友圈数量是否有变化。

此时，显然`self.fa`中里要新append上一个元素。然后再扫描此节点和其他节点的关系，适当更新fa即可。

此外这个算法好像还有个小bug，当最后一次union完了之后，被union的那个分量的非根节点，此时信息都还没被更新。
要解决这个似乎只能最后再针对所有位置再find一遍。
>关于上述bug的解决办法，除了在结束所有节点的遍历后再全部用find遍历一遍之外还可以这么搞：
>
>上述有问题的节点，虽然目前其指向的根节点还是老版本的，但是肯定不是其本身。
>因此在统计分量个数之类的问题中，对于最终的fa，可以检查`fa[i] == i`的个数，这样即便有一些节点对应的根节点没有被更新，
>也不会发生错误的统计。