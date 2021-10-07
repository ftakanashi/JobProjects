## 题目描述
请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。

实现 PeekingIterator 类：
- PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
- int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
- bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
- int peek() 返回数组中的下一个元素，但 不 移动指针。

示例：
```
输入：
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
输出：
[null, 1, 2, 2, 3, false]

解释：
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,2,3]
peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,2,3]
peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,3]
peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
peekingIterator.hasNext(); // 返回 False
```

提示：
```
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
对 next 和 peek 的调用均有效
next、hasNext 和 peek 最多调用  1000 次
```

- 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

### 解法 设置一个额外容器
这个题有点迷。。解读一下题意，就是说提供给你一个现成的Iterator类，这个类实现了`next`,`hasNext`这两个迭代器最主要的方法。

然后现在要求是在原有的`Iterator`类外面包一层`PeekIterator`类，这个类在要有迭代器`hasNext`和`next`的基础上，还有一个`peek`方法，能够随时看到下一个被迭代的元素是啥且不将其迭代出来。

其实思路上也没什么可说的。
内部的iterator显然可以直接实现`next`和`hasNext`功能。
问题就在于，当`peek`时该如何处理。显然内部iterator无法做到直接peek。
于是就想到了，可以在`PeekIterator`中额外设置一个容器，用来保存"下一个"数据。

也就是说，内部的iterator，其实际迭代进度总是比外部PeekIterator迭代的进度快一个元素。
当外部调用了`next`方法，实际上只需要返回额外容器中的内容，并且内部iterator向后迭代一个值，将迭代出来的放入容器。

这样的做法唯一一个需要想一下的地方就是`hasNext`的返回。
显然，当内部iterator的hasNext还是True，那么外层的肯定也是返回True。
另外，若内部是False了，只要容器中还有值，说明还有一个值未被迭代，因此也返回True。
除此之外返回False。

真没啥可说的了…
