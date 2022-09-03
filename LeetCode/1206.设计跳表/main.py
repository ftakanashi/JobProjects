#!/usr/bin/env python
import random

P = 0.25
MAX_LEVEL = 32


def random_level():
    level = 1
    while level < MAX_LEVEL and random.random() < P:
        level += 1
    return level


class SkiplistNode:
    def __init__(self, val, level):
        self.val = val
        self.next = [None for _ in range(level)]

    def __repr__(self):
        return f"<SLNode> {self.val}"


class Skiplist:

    def __init__(self):
        self.head = SkiplistNode(-1, MAX_LEVEL)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < target:
                curr = curr.next[l]
        return curr.next[0] is not None and curr.next[0].val == target

    def add(self, num: int) -> None:

        curr = self.head
        update = [self.head for _ in range(MAX_LEVEL)]
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < num:
                curr = curr.next[l]
            update[l] = curr

        new_node_level = random_level()
        self.level = max(self.level, new_node_level)
        new_node = SkiplistNode(num, new_node_level)
        for i in range(new_node_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        curr = self.head
        update = [self.head for _ in range(self.level)]
        for l in range(self.level - 1, -1, -1):
            while curr.next[l] and curr.next[l].val < num:
                curr = curr.next[l]
            update[l] = curr

        if curr.next[0] is None or curr.next[0].val != num:
            return False

        del_node = curr.next[0]
        for l in range(self.level):
            if update[l].next[l] != del_node:
                break
            update[l].next[l] = del_node.next[l]

        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)