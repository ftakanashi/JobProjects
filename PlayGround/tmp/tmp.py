#!/usr/bin/env python

def key(x):
    return x

l = [2,4,1,5,6]
l.sort(key=key)
print(l)