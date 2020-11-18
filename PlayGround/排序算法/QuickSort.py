#!/usr/bin/env python
# -*- coding:utf-8 -*-

def QuickSort(lst):
    partition(lst, 0, len(lst) - 1)

def partition(lst, left, right):
    if left >= right: return
    i = j = left + 1
    while j <= right:
        if lst[j] < lst[left]:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1
    i -= 1
    lst[i], lst[left] = lst[left], lst[i]
    partition(lst, left, i - 1)
    partition(lst, i + 1, right)

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    QuickSort(test_data)
    print(test_data)