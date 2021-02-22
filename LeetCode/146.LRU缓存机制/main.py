#!/usr/bin/env python
class BiDirLinkNode:
    def __init__(self, val, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = BiDirLinkNode(None)
        self.tail = BiDirLinkNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, node: BiDirLinkNode) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        val = self.d[key].val
        self.move_to_end(self.d[key])
        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if len(self.d) == self.capacity:
                old = self.head.next
                self.d.pop(old.key)
                self.head.next = old.next
                old.next.prev = self.head
                del old
            new_node = BiDirLinkNode(value, key)
            self.move_to_end(new_node)
            self.d[key] = new_node
        else:
            self.d[key].val = value
            self.move_to_end(self.d[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)