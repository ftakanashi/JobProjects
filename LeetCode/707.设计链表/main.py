#!/usr/bin/env python

class LinkNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index >= self.length: return -1
        i, p = 0, self.head.next
        while i < index:
            p = p.next
            i += 1
        return p.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkNode(val)
        tmp = self.head.next
        new_node.next = tmp
        tmp.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = LinkNode(val)
        tmp = self.tail.prev
        tmp.next = new_node
        new_node.prev = tmp
        self.tail.prev = new_node
        new_node.next = self.tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length: return
        if index < 0: index = 0
        i, p = 0, self.head.next
        while i < index:
            p = p.next
            i += 1
        new_node = LinkNode(val)
        tmp = p.prev
        tmp.next = new_node
        new_node.next = p
        p.prev = new_node
        new_node.prev = tmp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        i, p = 0, self.head.next
        while i < index:
            p = p.next
            i += 1
        tmp = p.next
        p.prev.next = tmp
        tmp.prev = p.prev
        self.length -= 1
        del p

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)