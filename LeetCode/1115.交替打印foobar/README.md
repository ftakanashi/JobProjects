## 题目描述
我们提供一个类：
```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。


示例 1:
```
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
```
示例 2:
```
输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
```

### 解法 使用threading.Semaphore信号量进行线程间通信
一道基本的多线程题目。
这个多线程模型也是经典的"生产者-消费者"模型。
foo函数是生产者，bar函数是消费者。

这题的问题就在于，如何确保消费者在生产者生产完之前不消费；生产者在消费者消费完之前不生产。

这里给出的一种方案是使用`threading.Semaphore`。
这也是一个`threading.Lock`的子类。
他在内部维护一个值`value`，每当其被acquire一次，这个值就减去1；每当其被release一次就加1。
当value是0的情况下被acquire的时候，线程会被挂起。

初始化时设置一个生产者Semaphore值为1，消费者Semaphore值为0。

并且在执行print之前将两个锁都acquire上。
此时因为消费者的锁值是0，所以消费者挂起。
生产者无问题。

生产者生产完成后，再将消费锁release掉。此时代码继续运行，到下一次acquire生产锁。
但是生产锁此时是0，因此生产者挂起。

另一方面，消费锁因为生产者的release，值为1，消费者线程开始工作进行消费。
消费完成后因为要让生产者继续生产，所以release生产锁。

如此，在A的工作流程中，先acquire A的锁，工作，再release B的锁。
两个角色都这么搞，就可以保证正常地工作。