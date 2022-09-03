## 题目描述
不使用任何库函数，设计一个 跳表 。

跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

了解更多 : https://en.wikipedia.org/wiki/Skip_list

在本题中，你的设计应该要包含这些函数：
```
bool search(int target) : 返回target是否存在于跳表中。
void add(int num): 插入一个元素到跳表。
bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
```
注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

示例 1:
```
输入
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
输出
[null, null, null, null, false, null, true, false, true, false]

解释
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
```

提示:
```
0 <= num, target <= 2 * 104
调用search, add,  erase操作次数不大于 5 * 104 
```

### 跳表的定义
这道题介绍了一种挺有意思的数据结构，跳表（Skip List）。
这种数据结构的概念本身就不多说了，题干里已经有了比较详细的介绍，也给出了资料。

简单来说，就是围绕着这样一张图：
![](https://assets.leetcode-cn.com/solution-static/1206/1206_1.PNG)

最宏观的角度来看，跳表本身还是一个一维单向链表，其节点带有一个值以及指向下一个节点的指针。
但和普通链表的不同之处在于，首先其实一个有序的链表，而更重要的，是其中的每个节点都有一个层级的概念。

上面图中，我们称最下面的层为第一层（下标为0），最上面为第四层（下标为3）。以后都以下标来称呼层级。
跳表的精髓在于，所有节点都会出现在第一层，而第`i`层的某个节点会有`P`的概率出现在第`i+1`层。
注意，最大层级和转移概率`P`都是超参数。

因此，在普通的一维线性结构的基础上，随着随机因素的引入，衍生出了跳表的二维结构。

那么二维结构有什么用呢？最显而易见的一点，就是随着一维变成二维，在其中搜索一个值的复杂度会从`O(n)`降低到`O(logn)`。
类似我们把有序一维链表变成了一个二叉搜索树。

正如题目所要求的那样，和其他的数据搜索结构类似，跳表基本上需要实现以下三个操作：

- 搜索
- 插入
- 删除

下面分别用语言先来描述一下各个操作的算法。

#### 搜索

从最上层开始，我们尝试遍历每层的节点。当碰到某个节点的下一个节点大于（注意，不取等号）搜索目标值 target 时，我们降低一个层级，从这个节点开始继续搜索。

可以想象，这个过程最终会来到第0层。而所有节点都在第0层有存在，所以只要 target 确实存在于跳表中，那么一定可以找到并且其一定是当前节点的下一个。

否则，就可以返回False。

#### 插入

插入略微繁琐一些。
首先和搜索一样，要从最上层开始往下按照同样的规则向下搜索。过程中我们还需要记录那些跳转节点的值，方便后续找到新插入的节点应该放在什么位置。

然后我们需要知道新插入节点的层级，这是一个需要随机的过程。具体来说，我们可以实现如下一个函数来随机获取一个层级。这也是转移概率`P`在代码中唯一体现作用的地方。

```python
import random
P = 0.25
MAX_LEVEL = 32
def random_level():
    level = 1
    while level < MAX_LEVEL and random.random() < P:
        level += 1
    return level
```

然后我们到各个层级中，把新节点接入即可。

#### 删除

删除和插入类似，首先还是要遍历层级，找到各个层级中被删除节点前一个的那些节点。这个过程还可以顺便确认一下被删除节点是否真的存在。若不存在直接返回False即可。

接着，我们对各个层级进行扫描，把要删除的节点去掉即可。

### 解法 跳表的实现

下面来具体讲怎么实现。
最直观的一种办法， 是维护多个层级的普通链表，但是那样会发现到后面会很麻烦。
所以跳表有其特有的一种套路。其节点的数据结构如下：

```python
class SkiplistNode:
    def __init__(self, val, level):
        self.val = val
        self.next = [None for _ in range(level)]
```

也就是说，节点之间互相连接，但同时用`self.next`来体现了各个层级之间的连接关系。`self.next`的长度则是节点的深度。

如上面图中的例子，第一个节点`3`的`next`是`[7, ]`。而第二个节点`7`的`next`就是`[11, 19, 37, None]`。

而SkipList类本身的初始化，以及搜索方法可以像下面这样写：

```python
class Skiplist:

    def __init__(self):
        self.head = SkiplistNode(-1, MAX_LEVEL)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < target:
                curr = curr.next[l]
        return curr.next[0] is not None and curr.next[0].val == target
```

可以看到，由于要顾及到所有层级的可能性，`self.head`的深度初始化为最大深度。另外还需要维护一个这个跳表的最大有效深度`self.level`。也就是说非head节点的最大深度，上图例子中`self.level`是4。

搜索方法则基本遵照上面的算法描述。
从最上层开始一层层向下扫描，每一层中找到值小于 target 的最大节点。当到达第0层后，只需要判断`curr.next[0]`是否为None以及不为None时值是否为target即可。

搜索这段代码后面还会用到，需要好好理解。
注意 `curr`是一个节点，而`curr.next[x]`的意思其实是在第x层的curr节点的下一个节点。这个和普通链表有很大不同，需要好好体会。

接下来是add方法：

```python
    def add(self, num: int) -> None:

        curr = self.head
        update = [self.head for _ in range(MAX_LEVEL)]
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < num:
                curr = curr.next[l]
            update[l] = curr

        new_node_level = random_level()
        self.level = max(self.level, new_node_level)
        new_node = SkiplistNode(num, new_node_level)
        for i in range(new_node_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
```

上半段代码和搜索很类似，只不过我们额外开了一个`update`数组用于保存那些每个层级中，小于`num`的最大节点是谁。
考虑到新节点的深度是新随机出来的，最大可能到达`MAX_LEVEL`，所以update的长度也得开到`MAX_LEVEL`。

下半段，我们首先新随机出一个深度，同时更新可能的跳表最大有效深度。
接着，从第0层开始向上遍历，将新节点接入跳表即可。

最后是删除的`erase`方法：

```python
    def erase(self, num: int) -> bool:
    
        curr = self.head
        update = [self.head for _ in range(self.level)]
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < num:
                curr = curr.next[l]
            update[l] = curr

        if curr.next[0] is None or curr.next[0].val != num:
            return False

        del_node = curr.next[0]
        for l in range(self.level):
            if update[l].next[l] != del_node:
                break
            update[l].next[l] = del_node.next[l]

        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return True
```

最上一段代码和add方法类似，还是通过扫描与update保存那些可能是被删除节点的前一个的节点们。
考虑到可能值为`num`的节点本身就不存在，所以第二个片段做了一个简单的判断。

终点在第三段，当运行到第三段时我们可以肯定，被删除节点是存在的，于是我们从下向上遍历各个层级，根据记录的那些“前一个节点”们，进行被删除节点的摘除。同时需要注意，被删除节点的深度不一定恰好是跳表最大有效深度，所以当`update[l].next[l]`不再是`del_node`，说明被删除节点能够覆盖的所有有效深度都已经被处理过了，所以可以直接break。

最后，随着一个节点被删除，我们可能还需要更新跳表最大有效深度。
这里用了一个比较粗暴的办法，就是删除后直接看哪些深度`self.head.next[l]`直接是None了，那些深度就已经不再是有效深度。不断减小`self.level`即可。

以上就是全部实现过程了。建议再看看代码好好体会一下。。。

