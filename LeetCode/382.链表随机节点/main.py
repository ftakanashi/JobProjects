#!/usr/bin/env python
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.elems = []
        i = head
        while i is not None:
            self.elems.append(i.val)
            i = i.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.elems)

class Solution2:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        p = self.head
        if p is None: return
        count = 1
        res = None
        while p is not None:
            if random.randint(1, count) == 1:    # 以1/count的概率覆盖记录
                res = p.val
            p = p.next
            count += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()