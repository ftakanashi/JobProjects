# 概要
堆本质上是一个连续表。

这个连续表符合一定的要求。
即把这个连续表按从上到下从左到右的顺序构建成一个完全二叉树时，
这棵树从根节点开始到任意一个叶节点的任意一条路径都是单调不递减（小顶堆）或者不递增（大顶堆）的。

不同路径之间完全独立不影响。

# 基本性质
由于是连续表表示的完全二叉树，一个重要的性质就是

>连续表中下标为`i`的节点N，其在二叉树中的父节点P，在连续表中的坐标是`(i - 1) // 2`。
>
>N的左右子节点L和R，（如果存在）下标分别是`i * 2 + 1`和`i * 2 + 2`。

# 代码实现

## 基础构建
```python
class Head:
    def __init__(self, elist):
        self._elems = list(elist)
        if elist:
            self.buildHead()

    def isEmpty(self):
        return len(self._elems) == 0

    def peek(self):
        if self.isEmpty():
            raise ValueError('Heap Empty.')
        return self._elems[0]
```
`buildHeap`方法暂且不说。
在上面的构建的基础上，下面加上各种堆相关的基础方法。
注意这次构建的堆，是小顶堆。

## 新加入元素与向上筛选(shift up)
由于本体是一个list，所以新加入元素最基本操作就是append没有毛病。
只是，单纯在elems后面append元素之后，如何维护堆的结构是个问题。此时就要用到shift up。

```python
    def enqueue(self, e):
        self._elems.append(e)
        self.shiftup(e, len(self._elems) - 1)

    def shiftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and elems[j] > e:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
```

很好懂，就从最后一个元素开始沿着路径依次上扫描，碰到合适的位置插入即可。

这样即可保证这条路径是符合堆序的。

## 取出堆顶以及向下筛选
在堆排序等其他 堆的应用过程中，取出堆顶元素是一个很重要的操作。比方说小顶堆的话，堆顶总是保持整个树上最小的那个值，
天然就可以做排序了。

取出堆顶后，显然剩下的左子树和右子树，要怎么整合起来是个问题。
想法是这样的，当拿走堆顶元素，其左右子树各自都还是一个堆。同时，拿走原堆
最后一个元素，此时还是一个堆。

拿走的最后一个元素当成是代替根节点的位置，放到最顶上。
此时显然这个树不再是一个堆了，就要恢复堆序。此时从堆顶开始向下筛选。
具体过程是比较堆顶元素e和左右子树根节点l和r。如果e是三者中最小，那么显然已经是堆。
否则，将最小的那个和e互换。然后重新判断e和他新的两个子节点之间值的关系。
子节点不存在就认为是无穷大。
总有一天，e会是它和两个子节点中最小的，此时局部堆形成，向下筛选就完成了。

代码
```python
    def dequeue(self):
        if self.isEmpty():
            raise ValueError('Empty Heap')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()    # 注意这个e是最后一个元素而不是e0
        if len(elems) > 0:
            self.shift_down(e, 0, len(elems))
        return e0

    def shift_down(self, e, start, end):
        elems, i, j = self._elems, start, start * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                # 右节点更小的情况
                j += 1
            if e < elems[j]:
                break  
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e              
```

至此，基本的堆操作就都有了

## 堆的构建
哦对了，之前还有个buildHeap的坑没有填。

注意到，从`len(elems) // 2`节点开始（不包括本身），所有的节点都是叶节点。这些叶节点本身都是一个堆了。
因此，建堆操作是从这个节点开始，依次向左向上分别建立子堆。当某个节点的左右两个子树是两个子堆，那么这个节点
再来一次shift down就可以把他自己变成一个堆。基于这个思想，向左向上依次shift down即可。

这也是为什么shift down方法的实现留了start和end作为接口而不是直接写死。因为它还可以被用来进行建堆操作。

代码很简单：
```python
    def buildHeap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.shift_down(self._elems[i], i, end)
```

作为结论可以记住的是，堆构建过程是O(n)的。