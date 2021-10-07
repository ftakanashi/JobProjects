#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None: return None    # 特殊情况

        def rec(node):
            tail = node
            while node is not None:

                if node.child is not None:
                    # 将子链表拉平后插入node与node.next之间
                    part_tail = rec(node.child)
                    tmp = node.next
                    node.next = node.child
                    node.child.prev = node
                    part_tail.next = tmp
                    if tmp:  tmp.prev = part_tail    # 注意node.next可能是None，因此这里做个简单判断

                    node.child = None    # 别忘了这步，如果不消除child的指向，leetcode判定返回的不是标准双向链表

                    # 维护最新的tail并且移动node指针继续扫描，child是None的情况，即下面else分支也是类似
                    tail = part_tail
                    node = tmp
                else:
                    tail = node
                    node = node.next

            return tail

        rec(head)
        return head