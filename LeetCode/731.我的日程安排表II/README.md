## 题目描述
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。

每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。

请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例：
```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
解释： 
前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。
```

提示：
```
每个测试用例，调用 MyCalendar.book 函数最多不超过 1000次。
调用函数 MyCalendar.book(start, end)时， start 和 end 的取值范围为 [0, 10^9]。
```

### 解法 差分数组
和`LC.729`不同，在不使用线段树的情况下，这里很难用有序集合之类的数据结构进行优化了。
时间复杂度避不开`O(n^2)`了。。

直接暴力差点意思，所以这里采用差分数组的做法。
另一方面，由于start和end的取值范围会很大，所以不能直接用数组来保存差分信息，这里得用哈希表。
而用了哈希表就意味着每次调用book方法都会不可避免地按序遍历整个哈希表，这也是这个做法`O(n^2)`复杂度的由来了。

实现细节上，当book被调用的时候我们直接将`diff[start] += 1`以及`diff[end] -= 1`。
然后按序遍历所有已经被记录的节点并进行差分值的计算。
根据题意，差分值不能超过2。一旦超过2，就该返回False了，当然，在那之前，由于本次调用的`start, end`区间并没有成功预约，所以记得要回退。

以上。