#!/usr/bin/env python

def quick_sort(lst):

    def parition(start, end):
        if start >= end: return
        pivot = lst[start]
        i = j = start + 1
        while j <= end:
            if lst[j] <= pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
            j += 1
        i -= 1
        lst[i], lst[start] = lst[start], lst[i]
        parition(start, i - 1)
        parition(i + 1, end)

    parition(0, len(lst) - 1)

if __name__ == '__main__':
    l = list(range(10))
    import random
    random.shuffle(l)
    print(l)
    quick_sort(l)
    print(l)