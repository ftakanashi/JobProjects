## 题目描述
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 AllOne 类：
```
AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
```

示例：
```
输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
```

提示：
```
1 <= key.length <= 10
key 由小写英文字母组成
测试用例保证：在每次调用 dec 时，数据结构中总存在 key
最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 104 次
```

### 解法 哈希表 + 双向链表
先补充一下，这题题目中没有给出一个额外的限制条件，那就是实现的所有方法必须都是O(1)的复杂度的。（不考虑字符串本身的长度带来的复杂度

如果没有这个限制，那么容易想到的一个办法就是用一个哈希表维护计数，然后在get的时候扫描所有计数找最大值或者最小值就行了。
但是由于要O(1)，而后者显然是一个线性操作，此时就需要思考了。

一个比较容易想到的思路是用一个反向的哈希表来记录`计数: 字符串`关系，
但是那样在get的时候仍然需要扫描所有计数值来找结果。

观察到，`inc`和`dec`这两个操作会不定时发动，而一旦发动，数据结构就会发生变化从而导致get的结果可能出现变化。
从这点，容易联想到LRU那样的结构。即每操作一次都需要更新内部的一些信息保证其他的方法工作正常。

LRU嘛，双向链表咯。

于是，这题的思路就有了。
首先，核心仍然是一个字符串计数的哈希表。只是哈希表的值指向一个双向链表中的各个节点。
每个节点代表了一种计数值以及其对应的所有字符串（可以用一个集合来维护）。
所以这个链表节点类长这样：
```python
class LinkListNode:
    def __init__(self, count, words=None, prev=None, next=None):
        self.count = count
        self.keys = set()
        self.prev = prev
        self.next = next
        if words is not None:
            for word in words: self.keys.add(word)
```

只要我们保证链表从左到右是根据节点中计数值排序的，那么get的两个方法就很好解决了。
分别随便取`head.next.keys`以及`tail.prev.keys`中的任意一个字符串即可。
初始化链表时，head的count初始化为0，tail的初始化为无穷大。

另一方面，inc和dec方法的难度有所增加。
以inc为例。
首先对于传递来的新单词`key`，需要判断其是否已经在哈希表中，

若是，说明之前处理过此单词，并且次单词已经指向了某个链表节点。
此时我们需要检查其下一个节点的count值是否恰好是当前count值+1，从而决定是否需要新建一个节点插入链表。
此外还不能忘记将当前节点的keys中，删去该单词。

若否，则需要考虑链表中是否有count值为1的节点，若没有还需要新建一个，插入到head后面。

总之，仔细想想的话逻辑能盘出来。更多逻辑就看代码吧。

dec也是类似的。