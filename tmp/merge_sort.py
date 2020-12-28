#!/usr/bin/env python
# -*- coding:utf-8 -*-

def MergeSort(lst):

    def rec_sort(lst, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        rec_sort(lst, start, mid)
        rec_sort(lst, mid + 1, end)

        i, j = start, mid + 1
        res = []
        while i <= mid and j <= end:
            if lst[i] <= lst[j]:
                res.append(lst[i])
                i += 1
            else:
                res.append(lst[j])
                j += 1

        while i <= mid:
            res.append(lst[i])
            i += 1
        while j <= end:
            res.append(lst[j])
            j += 1

        lst[start:end+1] = res

    rec_sort(lst, 0, len(lst) - 1)

if __name__ == '__main__':
    import random
    data = list(range(10))
    random.shuffle(data)
    print(data)
    MergeSort(data)
    print(data)