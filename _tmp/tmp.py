#!/usr/bin/env python

class MyClass:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MyClass, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    print(a is b)