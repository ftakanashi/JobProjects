## 题目描述
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：
```
void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
```
示例：
```
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
```

提示：
- 0 <= key <= 106
- 最多调用 104 次 add、remove 和 contains 。

### 解法 取模+链表哈希实现
题目不难，当做是一个对哈希实现的回顾。

实现一个哈希机制，最重要的是决定哈希函数本身以及发生哈希冲突时的处理方法。
这里针对这两个问题都采用最简单的处理办法。

第一，哈希函数，由于题目的输入全是数字，所以可以直接用取余的办法。
一个小trick：**在将取余作为哈希函数时，将哈希的size设置成一个较大的素数可以尽可能地避免冲突**

第二 哈希冲突的处理方法。理论上有很多种处理的办法，这里采用最简单的一种"链表法"。
即针对每一种哈希取值，其对应的不是一个保存一个值的变量，而是一个容器，可以按顺序将各个值安排进容器中。
这么做的坏处就是当哈希冲突发生的较多且集中在某些取值上时，表会很长，这导致remove，contains这些操作会趋向于线性而不是O(1)。

实现不困难，就不说了。
（虽说处理哈希是链表方法，但是实际上也没必要自己安排一个链表，用list这个顺序表足够了）

### 额外补充
Python内的哈希表和哈希集合大体上也是通过上述框架实现的。

关于哈希函数，Python内置了一个`hash`函数，这个函数可以将所有可被哈希的对象转化成一个大整数。
注意每次重新运行Python程序时，都会随机初始化一个哈希种子，所以即便是同一个值，不同次程序运行的`hash(x)`值会不同。
但是每次运行中，可以保证同样的值被hash之后肯定是相同的。

如果想在不同运行中都保持同样的hash值，则需要利用hashlib库。