# Python的垃圾回收

## 引用计数
在比较底层的语言比如C/C++中，程序员有时需要手动对变量进行整理，将不再使用的变量手动回收。
这里，回收是指去除变量名和数据之间的联系，并且将保存数据的那一部分内存空间清空。

在Python中显然不需要这么干。这主要是因为Python内部采用了引用计数机制来实时地维护所有程序中的变量。

所谓引用计数，是PyObject类的固有属性。我们知道Python中所有的对象，都是基于object这个基类，而这个类其实又是由C语言
实现的PyObject这个类。这个类中带有一个属性`obj_refcnt`进行引用计数的维护。

那么引用计数具体怎么用。具体来说，当一个对象在代码中发生如下事件时，其引用计数会加一：
```text
被创建（对于不可变对象来说是初次建立引用关系），如 a = 1
被引用，如 b = a
作为参数被传入函数
被放入某种容器数据结构比如list,dict等
```

反之，如果发生如下事件则引用计数减一：
```text
被del
离开作用域
所在容器被销毁或者被从容器中删除
```
使用内置的`sys.getrefcount`函数可以查看某个对象当前的引用计数。因为任意一个对象传入这个函数时根据规则计数都会+1，所以实际上返回的结果总是比
实际的计数大1。

## 垃圾回收
上面我们知道了每个对象都自带引用计数。

当某个对象引用计数减小为0，那就说明已经没有任何指针指向这个对象，此时可以放心地回收这部分空间。
这就是基于引用计数进行垃圾回收的原理。

利用引用计数进行垃圾回收，好处在于逻辑很简单，同时具有实时性。但是也有一些缺点，比如需要额外维护引用计数，当容器引用层级较深时可能遍历其中对象
比较耗时。
然而其最大的一个缺点是无法处理循环引用。这也意味着Python不能只用引用计数作为垃圾回收的依据。

### 循环引用
顾名思义，当a,b两个对象互相引用对方就是循环引用。循环引用也包括自己引用自己的情况。
这么搞会出什么问题？

首先，两个对象创建后的引用计数都是1，而在互相引用对方之后都变成了2。
此时如果del掉a,b两个对象名，那么计数减1。然而他们互相引用形成一个环，这个环外部没有对他们的任何引用但是因为这个环的存在，他们的计数无法减为0。
因为计数不能减为0，所以不能回收，因为不能回收，所以就发生了内存泄漏。

## 解决方案：标记-清除算法
如上所述，单纯参考引用计数进行垃圾回收无法解决循环引用的问题，因此这里导入标记-清除算法作为补充。

这个算法的描述见参考
>https://zhuanlan.zhihu.com/p/83251959

简单来说，其实整体的引用可以看做一个以对象为节点，以引用为边的有向图。
现在遍历图中每个节点，将其引用数减去一。注意这里的遍历单纯指遍历节点，因为这个图可能没有连通。

之后，再遍历图寻找那些引用计数还大于0的节点。此时引用计数还大于0，说明在图的外部有对这些节点的引用，因此这些节点不能当做垃圾回收。
从这些节点出发，遍历图，这次基于边遍历。由于图可能不连通，因此只能遍历到这些节点所在的联通分量。

这些连通分量上的节点，即使引用计数为0了，此时还是REACHABLE的因此不能被回收。相反，如果在上述遍历图过程中没遍历到的节点，说明已经没有任何用处，
因此放入UNREACHABLE分组，后续进行删除。

最后，别忘了上述修改引用计数的事情只是为了找出哪些节点是不再需要的unreachable节点，实际上并没有必要修改引用计数，因此上述操作都应该在
一个原图的拷贝上做。

以上就是标记-清除法的大概思想了。

## 解决方案：分代回收
确切来说，分代回收并不是一个独立的方案，可以看做是对标记-清除以及其他一些方法的优化。

一个客观事实：在实践中，被使用的内存中，通常有80%-90%都是"短命"的，即被使用没多久后就被回收。
所以可以将被使用的内存块分成0，1，2三个世代。数字越大的世代，其对应的内存块越长寿。长寿的定义是，经历过的gc扫描次数多。
比如某个0世代的内存块经历一次gc扫描后没被回收，那么他就被归入1世代；同理，1世代再经过一次扫描仍然健在，就归入2世代。

显然，长寿的内存块，经历了这么多次gc扫描都没被当垃圾回收，其是垃圾的概率就相应小。
在这个前提下，每次gc扫描可以优先扫描小的世代，从而提高扫描效率。

更具体的，分代回收为每个世代设置一个threshold，并且开始工作。
每当某个世代新增内存块数目超过threshold之后，gc就开始扫描这个世代以及所有更小世代，进行垃圾回收。
