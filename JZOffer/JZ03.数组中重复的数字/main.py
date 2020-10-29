#!/usr/bin/env python
# -*- coding:utf-8 -*-

# copied from nowcoder.com
# 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
# 函数返回True/False
def solution1(numbers, duplication):
    counter = {}
    for n in numbers:
        if n not in counter:
            counter[n] = 1
        else:
            duplication[0] = n
            return True

    return False

def solution2(numbers, duplication):
    i = 0
    while i < len(numbers):
        if numbers[i] != i:
            n = numbers[i]
            if n == numbers[n]:
                duplication[0] = n
                return True
            numbers[i], numbers[n] = numbers[n], numbers[i]
        else:
            i += 1
    return False

