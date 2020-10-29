## 题目描述

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

>输入：
>
>["CQueue","appendTail","deleteHead","deleteHead"]
>
>[[],[3],[],[]]
>
>输出：[null,null,3,-1]

示例 2：

>输入：
>
>["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
>
>[[],[],[5],[2],[],[]]
>
>输出：[null,-1,null,null,5,2]

提示：

- 1 <= values <= 10000
- 最多会对 appendTail、deleteHead 进行 10000 次调用

### 解法
熟知栈和队列特点就不难。说是特点其实就两个词儿，先进后出，和，先进先出。

栈永远是先进后出的，队列永远是先进先出的。

由此可以很容易想到一个解法。称两个栈分别为stack1和stack2。以stack1为主栈。
当发生appendTail的时候，元素直接push到stack1。当发生deleteHead的时候，先把除了栈底的其他
stack1中所有元素都拿出来放入stack2，pop出原栈底元素，然后再依次把stack2中的元素放回stack1。

由于两者都是先进后出，所以直接一个简单的循环就可以搞定，不需要额外的逻辑处理。

但是！

很显然，这种做法挺浪费操作的。如果stack1的长度很大比如有一万，为了deleteHead，
我要把9999个元素拿出来，再把他们放回去。这些都是浪费的。

注意到，当把上述9999个元素拿出来放入stack2之后，其实stack2的pop顺序就是原序列的逆序即实际上变成了
先进先出。

因此可以优化上述想法。基本想法还是不变，stack1作为主栈，stack2作为辅助。但是把stack1作为
专门处理appendTail的栈，而stack2专门处理deleteHead。

当appendTail发生时，还是不变，直接压入stack1。

当deleteHead发生时，如果stack2是空，那么为了拿到stack1此时的栈底元素，就把其所有元素依次pop出来并放入stack2。然后pop出stack2的栈顶元素。

如果stack2本身不是空的，说明此前发生过为了deleteHead把stack1全逆序放入stack2的过程。此时stack1中就算存在元素也都是晚于stack2中元素append
进来的。因此当stack2不是空的时候，直接pop其栈顶元素即可。

换句话说，之前的朴素想法中，pop完后把stack2的元素再充回stack1是没有必要的。
按照优化后方法操作可以节省一半操作时间。