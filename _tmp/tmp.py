#!/usr/bin/env python
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<ListNode {self.val}>'

def quick_sort(head):

    def swap(node1, node2):
        a, b = node1.val, node2.val
        node1.val, node2.val = b, a

    def partition(start, end):
        if start is end: return
        dummy = ListNode(-1, start)
        pivot = start.val
        prev = dummy
        k = start
        j = i = start.next
        while j is not end:
            if j.val < pivot:
                swap(i, j)
                i = i.next
                k = k.next
                prev = prev.next

            j = j.next

        swap(start, k)

        partition(start, prev)
        partition(k.next, end)

    partition(head, None)


if __name__ == '__main__':
    head = ListNode(3, ListNode(1, ListNode(5, ListNode(2, ListNode(4)))))
    head = []
    head = [1,1,2]
    head = [1,2,3,4,5]
    head = [5,4,3,2,1]

    quick_sort(head)
    i = head
    while i is not None:
        print(i.val, end=' ')
        i = i.next