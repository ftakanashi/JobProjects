## 题目描述

设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。

remove(val)：当 val 存在时，从集合中移除一个 val。

getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。

示例:
```javascript
// 初始化一个空的集合。
RandomizedCollection collection = new RandomizedCollection();

// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);

// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(1);

// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.insert(2);

// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.getRandom();

// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.remove(1);

// getRandom 应有相同概率返回 1 和 2 。
collection.getRandom();
```

### 解法
我做这道题的思路是这样的。

首先，整体的数据是一个可以重复的集合，但是不要求有顺序。那么作为基干很容易想到用list。
在此基础上，insert要求O(1)的话，使用append就可以了。

同时，getRandom要求和元素数目成线性正比，说得很高大上，其实仔细一想，就是针对一个列表抽样。
即`random.choice`。比如一个list中有99个1和1个0，getRandom自然很大概率会抽到1而非0。

问题在于remove上。

若采用普通的想法，有两个问题。
首先，remove要判断要删除的元素在不在list中，如果不在就返回False。
此时势必要检查所有元素，这就会导致O(n)了。

第二，如果找到元素，元素位于数组中间的某个位置，将其删除可以用`l.remove`之类的
方法，但是要知道这个方法本质上是顺序表的删除方法。即删除某个元素后，要将后序所有元素都依次前移，还是一个O(n)操作。

针对第一个问题，用O(1)时间检索元素，很容易就想到可以用哈希，即dict。即保存每个元素及其对应的下标信息。
由于允许重复元素存在，所以每个value可能不是一个单独值，而也是一个集合。这里其实用list或者set都可以。姑且默认使用set，后面再详细讨论区别。

针对第二个问题，肯定不能直接用remove方法，而是要我们手动来实现删除操作。因为这个数据结构本身对元素的顺序没有要求，
所以为了避免依次前移后序元素的操作，其实可以直接把末尾元素给补充到被删除位置来。如此就可以在O(1)的时间达到删除操作。

总结一下以上思路。首先这个数据结构的基干是一个list，其次，它内部还维护了一个`元素: 下标集合`的dict。
- insert操作直接在list后面append。
- remove操作是现在dict中检索，如果检索到对应元素则在list中对应元素位置置空，然后将list的末尾元素复制过来。
注意此时除了操作list本身，也要将dict的信息同步维护。当list中有多个对应元素时，方便考虑可以选取其中最靠后的元素作为
- getRandom操作就是简单的random.choice(list)即可。

最麻烦的应该还是remove的实现。

#### 关于dict的value是list还是set
首先补充一点以前可能忽视的知识。就是Python中的set。
set也有pop, remove, add等方法。尤其是其中的remove方法，是O(1)的，因为set内部也是hash实现的。这一点和list不一样。
至于set的pop，表现和list的pop一样，是先进后出的。

这块结合具体代码来说。最开始想到的还是用list。
但是如果用了list，则在维护下标dict的时候，最后元素前移时要同步维护下标信息，此时要删除原下标。

```python
i = self.i_map[val].pop()
j = len(self.container) - 1

val_j = self.container[j]
self.container[i] = val_j
self.i_map[val_j].add(i)    # 当然如果用了list这里应该是append
self.i_map[val_j].remove(j)   # ！这里
```

就像之前说过的，list的remove方法不是O(1)的，所以不太好。所以用了set。

值得注意的是，相比于list，set虽然时间上是O(1)了，但是天下没有免费的午餐，他还是用空间换时间的。

所以试验了一下，发现如果把dict的value结构从set换成list，那么运行时间虽然有几毫秒的增加，但内存消耗有所减少。