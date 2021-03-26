#!/usr/bin/env python

import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.produce = threading.Semaphore(1)
        self.consume = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.produce.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.consume.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.consume.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.produce.release()