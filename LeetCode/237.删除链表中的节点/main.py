#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # 2021/11/2追记 这个判断是没用的，因为 1.题目明确保证删除的不会是最后一个节点
        # 2.若node.next真是None，将node设置为None毫无意义。这只是一个引用指向的切换，而不会真的改变链表内节点数据结构
        if node.next is None:
            node = None
        node.val = node.next.val
        node.next = node.next.next