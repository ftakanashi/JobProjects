## 题目描述
请你设计一个日志系统，可以流式接收消息以及它的时间戳。每条 不重复 的消息最多只能每 10 秒打印一次。也就是说，如果在时间戳 t 打印某条消息，那么相同内容的消息直到时间戳变为 t + 10 之前都不会被打印。

所有消息都按时间顺序发送。多条消息可能到达同一时间戳。

实现 Logger 类：
```
Logger() 初始化 logger 对象
bool shouldPrintMessage(int timestamp, string message) 如果这条消息 message 在给定的时间戳 timestamp 应该被打印出来，则返回 true ，否则请返回 false 。
```
 

示例：
```
输入：
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
输出：
[null, true, true, false, false, false, true]

解释：
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // 返回 true ，下一次 "foo" 可以打印的时间戳是 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // 返回 true ，下一次 "bar" 可以打印的时间戳是 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11 ，返回 false
logger.shouldPrintMessage(8, "bar");  // 8 < 12 ，返回 false
logger.shouldPrintMessage(10, "foo"); // 10 < 11 ，返回 false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11 ，返回 true ，下一次 "foo" 可以打印的时间戳是 11 + 10 = 21
```

提示：
```
0 <= timestamp <= 10^9
每个 timestamp 都将按非递减顺序（时间顺序）传递
1 <= message.length <= 30
最多调用 10^4 次 shouldPrintMessage 方法
```

### 解法1 哈希表
很明显，这题需要解决两个问题。
第一，如何及时删除已经失效的日志。
第二，如何判断新来的日志内容是否和仍有效的日志发生冲突。

第二点很容易想到用哈希来做。
如果尝试用哈希表，那么显然值可以用timestamp。
接着第一点就迎刃而解了，针对某条msg存在于哈希表中，只需要判断其保存着的timestamp和当前时间点差是不是大于10。
若否，直接返回False。若是，则代表需要重新打日志了，就更新timestamp为当前时间即可。

当然，上述做法在实际的工作中几乎不会用。
因为键用了具体的日志内容而日志内容是千差万别的。如果不定期清理哈希表中过期的键值对，会导致哈希表越长越大。

### 解法2 队列 + 哈希集
针对上面提到的第一点，可能想到可以用队列来做。
队列中维护某条日志的内容以及时间。
在新来日志的时候，将所有时间点小于当前时间点-10的项从队列左边pop出去。

接着解决第二点，如何才能知道新msg是否存在于当前队列中？
线性扫描显然太麻烦，因此和队列并列地维护一个哈希集。
当有项从队列左边pop掉时，同步从哈希集中将其内容也remove掉。

这么做可以保证每时每刻内存中的内容都是处于有效期内的内容，不会浪费空间。
当然，因为要去pop掉一些项目。如果有大量同时发生的日志，这可能会导致线性的操作时间。

两种方法，各有利弊需要权衡。