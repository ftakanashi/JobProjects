## 题目描述
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，
并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 最短时间 。

示例 1：
```
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
```
示例 2：
```
输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类
```
示例 3：
```
输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
```

提示：
- 1 <= task.length <= 104
- tasks[i] 是大写英文字母
- n 的取值范围为 [0, 100]

### 解法 模拟
从直觉上来说，肯定是要优先安排任务次数多的任务的。

另外注意到，由于n的限制，在n+1个时间单位内，某个任务只能出现一次。

于是，下面的想法出现了。
统计一个counter，以n+1个时间单位为一个周期。
一个周期内，按照count的计数降序安排各个任务，并实时更新counter。
如果counter中count次数还大于0的任务种类不足n+1个了，那么就安排待命。
这个过程周而复始，直至counter中所有任务种类的计数都等于0。

模拟过程中维护一个time作为答案。
每次安排任务或者安排待命时+=1。
注意最后counter中所有任务种类计数都为0时，没必要继续安排待命，所以可以直接break。

代码中用了`collections.Counter`进行了实现。有`most_common`之类的接口，用起来很方便，代码因此比较简洁。

如果自己实现，可以就维护二元组的列表，可能速度上会加快但是代码比较繁琐。

> 2021/08/09 追加笔记
>
> 其实上述模拟解法，是遵从了贪心思想。这里贪的就是尽量早尽量多地安排执行次数多的任务。