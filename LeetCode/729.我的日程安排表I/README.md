## 题目描述
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的日程安排不会造成 重复预订 ，则可以存储这个新的日程安排。

当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 重复预订 。

日程可以用一对整数 start 和 end 表示，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end 。

实现 MyCalendar 类：
```
MyCalendar() 初始化日历对象。
boolean book(int start, int end) 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 true 。否则，返回 false 并且不要将该日程安排添加到日历中。
```

示例：
```
输入：
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
输出：
[null, true, false, true]

解释：
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。
```

提示：
```
0 <= start < end <= 109
每个测试用例，调用 book 方法的次数最多不超过 1000 次。
```

### 解法 有序集合
这题本身其实用暴力也能AC。
而更加精巧的用线段树的做法则因忘了线段树的事情了就不写了。。
这里就重点介绍如何使用Python中的有序集合来做。

有序集合，或者说有序哈希表，通过 `from sortedcontainers import SortedDict` 类似这样的方式导入。
此时，`SortedDict`类的实例基底是一个哈希表，但同时内部维护了哈希表的key的顺序。
因此其`sd.keys()`方法以及`sd.items()`方法的返回都是有序的列表。
甚至可以直接有`sd.bisect_left(target)`之类的调用，意思是找出所有key中第一个小于等于target值的key的位置（指`keys()`列表中的位置）

而这题，我们将所有日程`start, end`以`sd[start] = end`的形式维护起来。
每当来一个新的日程`x, y`时，我们只需要以`y`为目标值二分查找当前的所有日程，找到第一个start时间小于等于当前`y`的日程。
得到前一个日程的end时间点，`prev_end`。
只需要`prev_end <= x`，那么当前时间点就是可以加入日程而不冲突的。
否则则不行。

按照以上思路写代码即可。