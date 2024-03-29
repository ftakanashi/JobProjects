## 题目描述
给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。

返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。

示例1：
```
输入: head = [0,1,2,3], nums = [0,1,3]
输出: 2
解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。
```
示例 2：
```
输入: head = [0,1,2,3,4], nums = [0,3,1,4]
输出: 2
解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。
```

提示：
```
链表中节点数为n
1 <= n <= 104
0 <= Node.val < n
Node.val 中所有值 不同
1 <= nums.length <= n
0 <= nums[i] < n
nums 中所有值 不同
```

### 解法 哈希表 模拟
首先解释一下题意，有一个所有节点的值都不重复的单向链表，以及一个所有值都不重复的数组。

现在让你找出链表中有多少个连续的片段，其中每个片段的每个值都存在于数组中。

题设给出所有值都不重复，摆明了是要用哈希。
不过一开始太过于拘泥于值和链表节点之间的对应。实际上反过来对数组哈希会更加方便（而哈希在这里也只是一个优化手段，不哈希甚至也可以）。

具体的，我们扫描一次链表，扫描过程中检查当前节点是否是某一个片段的开头。
这主要就是检查当前节点的值是否存在于数组（或者哈希之后的哈希集）中，若是，则不断向后移动指针直到节点不存在与哈希集中或者移到了末尾。

每结束一个片段的遍历之后，就继续手动一个个往前移动。
以上。