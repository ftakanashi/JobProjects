## 题目描述
设计你的循环队列实现。 
循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。

它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。

在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。

但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
```
MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
```
 
示例：
```
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
```

提示：
- 所有的值都在 0 至 1000 的范围内；
- 操作数将在 1 至 1000 的范围内；
- 请不要使用内置的队列库。

### 解法 基于数组的循环队列
一个最最简单的实现方法，是利用Python的List长度可变的特点。
dequeue发生后，直接将数据结构内部的数组改成`[1:]`即可。

不那么投机取巧的话，那么就只能老老实实来做。
倒也不难，按照循环队列的定义思考即可。
注意，循环队列和一般队列的区别就在于，其enqueue的插入点和dequeue的弹出点不总是内部数组最后和最前。

因此，可以考虑维护两个指针始终指向插入点和弹出点。
更具体的定义，插入点是指当前队列tail元素的后一个位点，弹出点则指当前队列的head元素。

显然在enqueue一个元素后insert点后移，dequeue一个元素后pop点后移。

由于是循环队列，注意两者不能越界。一旦insert或者pop超过了k，显然就需要做对k取余的操作，表明其又循环到数据结构中数组的开头去了。