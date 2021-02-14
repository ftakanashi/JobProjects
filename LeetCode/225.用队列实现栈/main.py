#!/usr/bin/env python
import collections
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque([])
        self.queue2 = collections.deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q = self.queue1 if len(self.queue1) > 0 else self.queue2
        q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue1) > 0:
            q1, q2 = self.queue1, self.queue2
        else:
            q2, q1 = self.queue1, self.queue2

        while len(q1) > 1:
            q2.append(q1.popleft())

        return q1.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue1) > 0:
            q1, q2 = self.queue1, self.queue2
        else:
            q2, q1 = self.queue1, self.queue2

        while len(q1) > 1:
            q2.append(q1.popleft())

        v = q1.popleft()
        q2.append(v)
        return v

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()