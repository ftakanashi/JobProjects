#!/usr/bin/env python
import random
class LinkListNode:
    '''
    带计数值和相应keys集合的双向链表节点
    '''
    def __init__(self, count, words=None, prev=None, next=None):
        self.count = count
        self.keys = set()
        self.prev = prev
        self.next = next
        if words is not None:    # 初始化keys集合
            for word in words: self.keys.add(word)

class AllOne:

    def __init__(self):
        self.key2node = {}

        # 头尾节点的初始化，从而保证链表总是有序的
        self.head = LinkListNode(0)
        self.tail = LinkListNode(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.key2node:    # 若之前未处理过该key
            orig = self.head    # 操作即使发生，也发生在head之后
        else:    # 若之前处理过该key
            orig = self.key2node[key]    # 操作发生在orig节点后
            orig.keys.remove(key)    # 别忘了从orig的keys中删除key

        if orig.next.count > orig.count + 1:    # 要加新节点的情况
            a, b = orig, orig.next
            new = LinkListNode(orig.count + 1, [key, ])
            a.next = new
            new.prev = a
            b.prev = new
            new.next = b
        else:    # 不用加新节点
            orig.next.keys.add(key)
        self.key2node[key] = orig.next    # 更新哈希表

        if orig is not self.head and not orig.keys:
            # 若orig节点经过remove之后keys空了，说明不必要再将其维护在链表中，删除之
            orig.prev.next = orig.next
            orig.next.prev = orig.prev
            del orig

    def dec(self, key: str) -> None:
        orig = self.key2node[key]    # 题目保证key在dec前一定被inc过
        orig.keys.remove(key)
        if orig.prev.count < orig.count - 1:    # 要加新节点的情况
            a, b = orig.prev, orig
            new = LinkListNode(orig.count - 1, [key, ])
            a.next = new
            new.prev = a
            b.prev = new
            new.next = b
        else:    # 不用加新节点的情况
            orig.prev.keys.add(key)
        self.key2node[key] = orig.prev

        if not orig.keys:    # 同inc理 需要及时删除已经空了的节点
            orig.prev.next = orig.next
            orig.next.prev = orig.prev
            del orig

    def getMaxKey(self) -> str:
        return random.sample(self.tail.prev.keys, 1)[0] if self.tail.prev.keys else ""

    def getMinKey(self) -> str:
        return random.sample(self.head.next.keys, 1)[0] if self.head.next.keys else ""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()