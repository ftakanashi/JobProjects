#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p, s = head, 0
        s2node = {0: dummy}    # 记录前缀和值与节点之间的对应关系
        while p is not None:
            s += p.val
            s2node[s] = p    # 第一次遍历，记录前缀和值最后一次出现的位置
            p = p.next

        # 第二次遍历，重新计算前缀和并且指针从dummy开始
        p, s = dummy, 0
        while p is not None:
            s += p.val
            p.next = s2node[s].next    # 删除片段
            p = p.next

        return dummy.next