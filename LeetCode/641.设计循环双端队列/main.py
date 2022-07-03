#!/usr/bin/env python

class LinkNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_k = k
        self.k = 0
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.k == self.max_k: return False
        node = LinkNode(value)
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node
        self.k += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.max_k: return False
        node = LinkNode(value)
        tmp = self.tail.prev
        tmp.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = tmp
        self.k += 1
        return True

    def deleteFront(self) -> bool:
        if self.k == 0: return False
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        del node
        self.k -= 1
        return True

    def deleteLast(self) -> bool:
        if self.k == 0: return False
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        del node
        self.k -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.k == 0 else self.head.next.val

    def getRear(self) -> int:
        return -1 if self.k == 0 else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.k == 0

    def isFull(self) -> bool:
        return self.k == self.max_k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()