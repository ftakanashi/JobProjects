#!/usr/bin/env python

def gcd(x, y):
    if x < y: x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

def sct(x, y):
    g = gcd(x, y)
    return g * (x // g) * (y // g)

if __name__ == '__main__':
    lst = [2,6,20]
    s = sct(lst[0], lst[1])
    for i in range(2, len(lst)):
        s = sct(s, lst[i])
    print(s)