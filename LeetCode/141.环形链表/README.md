##题目描述
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。

如果 pos 是 -1，则在该链表中没有环

注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。


示例 1：
>输入：head = [3,2,0,-4], pos = 1
>
>输出：true
>
>解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
>输入：head = [1,2], pos = 0
>
>输出：true
>
>解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
>输入：head = [1], pos = -1
>
>输出：false
>
>解释：链表中没有环。
 

提示：
- 链表中节点的数目范围是 [0, 104]
- -105 <= Node.val <= 105
- pos 为 -1 或者链表中的一个 有效索引 。

### 解法1 遍历节点
很自然的想法就是从head开始遍历节点，没路过一个节点就把这个节点标记为已经路过过，当某个节点已经路过，显然就说明存在环了。

这个"标记"可以采用set在链表外部设置，也可以采用修改链表值的办法来实现，当然两者各有好坏。

答案的代码用修改链表值为None的形式来表示其已经路过。

### 解法2 快慢指针
一个很有意思的解法。

设想在链表开头设置一对快慢指针。快指针始终比慢指针多走一步。

当某个链表中存在环的时候，快指针势必会先入环，接着一段时间后慢指针也入环。此时两个指针就像在田径场跑步。
我们只需要判断快指针是否套圈了慢指针，就可以判断是否存在环。

如果快指针变成了None而从没追上过慢指针，说明不存在环。

由于只要有环，快慢指针就一定会有套圈现象，所以这个解法的各种边界不是那么严格。
比如我可以让快指针一次走两步，慢指针一次走一步。

判断是否有套圈可以判快慢指针是否指向同一个节点或者快指针下一个是慢指针这样。

总之怎么样都行，比较随便。