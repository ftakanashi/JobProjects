#!/usr/bin/env python
# Definition for singly-linked list.
from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        heap = [(h.val, i) for i, h in enumerate(lists) if h]
        heapq.heapify(heap)
        dummy = tail = ListNode(None)

        while heap:
            val, i = heapq.heappop(heap)

            node = lists[i]
            lists[i] = node.next    # 替换新head
            node.next = None    # 切断节点原有next连接

            tail.next = node    # 将节点收割进答案
            tail = tail.next    # 答案尾巴更新

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next