#!/usr/bin/env python
# -*- coding:utf-8 -*-

def MergeSort(lst):

    def recursive_sort(left, right):
        if left >= right:
            return
        mid = (left + right) // 2

        recursive_sort(left, mid)
        recursive_sort(mid + 1, right)

        i, j = left, mid + 1
        res = []
        while i <= mid and j <= right:
            if lst[i] <= lst[j]:
                res.append(lst[i])
                i +=1
            else:
                res.append(lst[j])
                j += 1

        while i <= mid:
            res.append(lst[i])
            i += 1
        while j <= right:
            res.append(lst[j])
            j += 1

        lst[left:right + 1] = res

    recursive_sort(0, len(lst) - 1)

if __name__ == '__main__':
    lst = [2,4,3,7,1,8,0,6,9,5]
    MergeSort(lst)
    print(lst)


