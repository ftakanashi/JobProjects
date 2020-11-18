#!/usr/bin/env python
# -*- coding:utf-8 -*-

def HeapSort(lst):

    def shift_down(lst, e, start, end):
        i, j = start, start * 2 + 1
        while j < end:
            if j + 1 < end and lst[j + 1] < lst[j]:
                j += 1

            if lst[j] > e:
                break
            lst[i] = lst[j]
            i, j = j, j * 2 + 1
        lst[i] = e

    end = len(lst)
    for i in range(end // 2, -1, -1):
        shift_down(lst, lst[i], i, end)

    for i in range(end - 1, -1, -1):
        e = lst[i]
        lst[i] = lst[0]
        shift_down(lst, e, 0, i)

    # reverse the sorted heap list
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    HeapSort(test_data)
    print(test_data)