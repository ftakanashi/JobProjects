#!/usr/bin/env python
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        i = head
        while i is not None:
            n += 1
            i = i.next

        if n <= k:
            res = []
            i = head
            while i is not None:
                res.append(i)
                tmp = i.next
                i.next = None
                i = tmp
            for _ in range(k - n): res.append(None)
            return res

        base_len = n // k
        res = []
        part_head = head
        for _ in range(n % k):
            i = part_head
            for _ in range(base_len): i = i.next
            tmp = i.next
            i.next = None
            res.append(part_head)
            part_head = tmp

        for _ in range(k - (n % k)):
            i = part_head
            for _ in range(base_len - 1): i = i.next
            tmp = i.next
            i.next = None
            res.append(part_head)
            part_head = tmp

        return res