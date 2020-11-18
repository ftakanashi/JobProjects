#!/usr/bin/env python
# -*- coding:utf-8 -*-

def MergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = MergeSort(left)
    right = MergeSort(right)

    # merge the sorted lists
    res = []
    i, j = 0, 0
    m, n = len(left), len(right)
    while i < m and j < n:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i < m: res.extend(left[i:])
    if j < n: res.extend(right[j:])

    return res

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    sorted_test_data = MergeSort(test_data)
    print(sorted_test_data)