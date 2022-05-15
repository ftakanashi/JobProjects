## 题目描述
设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

- insert(val)：当元素 val 不存在时，向集合中插入该项。
- remove(val)：元素 val 存在时，从集合中移除该项。
- getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

示例 :
```
// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomSet.insert(1);

// 返回 false ，表示集合中不存在 2 。
randomSet.remove(2);

// 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2 。
randomSet.getRandom();

// 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomSet.remove(1);

// 2 已在集合中，所以返回 false 。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
randomSet.getRandom();
```

### 解法 列表+哈希表
这题乍一看很傻比。但是仔细一品很有意思。

因为要求是所有操作都是O(1)的，所以第一时间很容易想到用一个set来保存所有的元素。
这样至少保证了insert和remove操作的O(1)。

但是这样的话getRandom很尴尬。
getRandom必然要用到random模块，可是random模块的各种方法基本都是要基于连续表的。

于是想，能不能以空间换时间，再设置一个列表维护已有元素。
可是这样的话如何同步set和list之间就有点问题。

比如remove元素的时候，从list里remove掉它需要O(n)。

于是拓展想法，不是用set，而是用dict。dict中维护list中值和下标的对应关系。

这样一来，insert的时候，实时维护新值和下标，getRandom的时候从list中random一个出来。
唯一的问题在于remove的时候，list中remove元素还是要扫描O(n)。

在这种场景，从list中删除一个指定元素但是要求O(1)时有这样一个套路：
pop并记录最后一个元素。然后将这个元素写到指定删除元素的下标位置。
这么做需要实时知道所有元素和下标的对应关系，当然这些关系在dict里有。

剩下的就是一些细节处理，比如remove掉的刚好是最后一个元素，或者remove掉后集合为空等。

#### 2022/04/13 一个更简化的代码版本
```python
import random
class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash: return False
        self.list.append(val)
        self.hash[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash: return False
        i = self.hash.pop(val)
        tail = self.list.pop()
        if i < len(self.list):
            self.list[i] = tail
            self.hash[tail] = i
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
```

另，今天看到这道题后第一反应是和`LC.432`记混了，尝试用哈希表+双向链表来做了。
思路倒也挺清晰，问题关键在于如何进行getRandom操作。
链表随机取节点，以为妥妥的蓄水池取样，但是回头看了下蓄水池采样才发现那个采样算法是O(n)的，所以就G了。