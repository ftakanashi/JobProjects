#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None: return None
        dummy = ListNode(-1, next=head)
        i = j = dummy
        while j.next is not None and j.next.next is not None:
            i = i.next
            j = j.next.next
        mid = i.next
        i.next = None
        r = mid.next
        mid.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(r)
        return root