#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        p = head
        ans = 0
        while p is not None:
            if p.val in nums:
                ans += 1
                while p is not None and p.val in nums:
                    p = p.next
            else:
                p = p.next

        return ans