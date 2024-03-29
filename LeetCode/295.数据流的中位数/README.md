## 题目描述
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，
```
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
```
设计一个支持以下两种操作的数据结构：
```
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
```
示例：
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```
进阶:
- 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
- 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

### 解法 双堆
此题同JZ41，同时和LC480.滑动窗口的中位数类似。

相比于480，这道题不涉及数据的删除，所以更加简单一些。

这里介绍的做法是维护两个堆，一个大顶堆一个小顶堆。
大顶堆维护数据流中比较小的一半数据，小顶堆维护比较大的一半数据。
换句话说，两个堆的堆顶就是最靠近数据中心的两个数了。

直觉上来说，只要尽量保持两个堆的元素数量相同或者只相差1，就可以轻松求出中位数。
比如两者元素数量相同，那么中位数就是两个堆顶的平均数。
如果两者相差1，我们可以规定大顶堆数字数量始终大于等于小顶堆，那么大顶堆的堆顶就是中位数。

按照上述思路就可以写代码了。

实现过程中需要注意，addNum时可能发生的情况是：
如果新加入的num大于大顶堆堆顶，那么这个num肯定是要加入小顶堆。
但是加入小顶堆后可能发生后者的长度大于前者，此时要`大顶堆.push(小顶堆.pop())`。

同理，如果新加入num小于大顶堆堆顶，那么num加入大顶堆，此时可能发生大顶堆的长度大于小顶堆+1。
此时要`小顶堆.push(大顶堆.pop())`。

只要维持上述规则，就可以将两个堆的长度限制在我们需要的范围内。

#### 2021/08/27 一版更好看的代码
上面解答还自己实现了堆，总体代码量比较大，不太好看。

今天写了个好看点的版本，附上。