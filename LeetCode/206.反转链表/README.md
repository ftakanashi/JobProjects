## 题目描述
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

### 解法0 利用外部空间
如果使用外部空间，那简单的一批。
显然时间空间都是O(n)的。

### 解法1 迭代
逐个扫描节点，在当前节点，在保存原next节点的情况下，将next指向前一个节点。
然后让当前节点成为上一个节点，原next成为当前节点，迭代即可。
时间O(n)空间O(1)

### 解法2 递归
没时间了，就贴个URL：https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/