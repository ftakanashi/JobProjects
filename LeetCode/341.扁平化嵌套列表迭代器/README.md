## 题目描述
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:
```
输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
```
示例 2:
```
输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
```

### 解法 栈
一道怪题…

首先注意看注释，上面给出了NestedInteger类的定义。
其实题目给的输入的那个列表，其中每个元素不是真正的int类型或者list，而是有这个类进行了一个外部的包装的。
所以要使用这个类的接口进行数值的处理。

另一方面，下方的注释给出了调用我们定义的类的方式。是
```python
while i.hasNext():
    v.append(i.next())
```

写核心代码的时候，要严格记住上面这个调用方式。

接下来写核心代码。显然遍历一个嵌套的数组，一个很自然的想法是用递归。
这里用栈来模拟递归。

如果一个输入全是普通数字，即这是个一维数组的话，那么就直接将其倒序入栈，然后栈中pop出来返回即可。
如果某个元素本身也是个数组，那么可以加个while循环，只要栈顶的元素不是int（那么其肯定是数组），就将其pop出来后
倒序充入栈。
这样即可以保证遍历的顺序性了。

但这样还有个潜在的小问题。
我将上述while循环写在了next方法中，类似于：
```python
def next(self) -> int:
    while self.stack and not self.stack[-1].isInteger():
        self.stack += self.stack.pop().getList()[::-1]
    if self.stack: return self.stack.pop().getInteger()

def hasNext(self) -> bool:
    return self.stack
```
这个代码下，类似于`[[[]]]`的用例无法通过测试。
因为输入没有任何数字，自然期待输出是空列表。
但是由于第一次判断hasNext的时候栈就是输入，是有内容的（虽然内容都是空列表），于是不可避免地会去执行next。
一旦执行next，无论如何都会有返回（比如返回None）。
这导致外部的结果容器最终将None收入其中，与预期不符。

正确的做法就是在上述空列表嵌套的输入时，杜绝next的执行，这就需要将while循环写入hasNext。