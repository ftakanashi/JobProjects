#!/usr/bin/env python
# Definition for singly-linked list.
from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
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


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return

        def merge(l, r):
            if l == r: return lists[l]
            mid = (l + r) // 2
            l_head = merge(l, mid)
            r_head = merge(mid+1, r)
            head = ListNode()
            tail = head
            while l_head and r_head:
                if l_head.val <= r_head.val:
                    tail.next = l_head
                    tmp = l_head.next
                    l_head.next = None
                    l_head = tmp
                else:
                    tail.next = r_head
                    tmp = r_head.next
                    r_head.next = None
                    r_head = tmp
                tail = tail.next
            if l_head: tail.next = l_head
            if r_head: tail.next = r_head
            return head.next

        return merge(0, len(lists) - 1)
