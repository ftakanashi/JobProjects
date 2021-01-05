#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:

    def toNum(self, head: ListNode) -> int:
        node = head
        res = 0
        while node is not None:
            res = res * 10 + node.val
            node = node.next
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.toNum(l1)
        n2 = self.toNum(l2)
        res = n1 + n2
        if res == 0:
            return ListNode(0)
        tail = None
        while res > 0:
            d = res % 10
            node = ListNode(d)
            node.next = tail
            tail = node
            res = res // 10
        return tail

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        carry = False
        tail = None
        while len(stack1) > 0 and len(stack2) > 0:
            n1 = stack1.pop()
            n2 = stack2.pop()
            res = n1 + n2
            if carry:
                res += 1
            carry = res >= 10
            res = res % 10

            node = ListNode(res)
            node.next = tail
            tail = node

        if len(stack1) > 0 or len(stack2) > 0:
            stack = stack1 if len(stack1) > 0 else stack2
            while len(stack) > 0:
                n = stack.pop()
                if carry: n += 1
                carry = n >= 10
                n = n % 10
                node = ListNode(n)
                node.next = tail
                tail = node

        if carry:
            node = ListNode(1)
            node.next = tail
            tail = node

        return tail