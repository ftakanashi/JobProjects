#!/usr/bin/env python

'''
有时候解决问题不需要完整的堆，函数实现更加轻巧
相当于实现了heapq中的各个库方法。
'''

def shift_down(lst, start):
    '''
    默认直接交换到最底层
    '''
    i, j = start, start * 2 + 1
    v = lst[start]
    while j < len(lst):
        if j + 1 < len(lst) and lst[j + 1] < lst[j]: j = j + 1
        if v <= lst[j]: break
        lst[i] = lst[j]
        i, j = j, j * 2 + 1
    lst[i] = v

def build_heap(lst):
    n = len(lst)
    for i in range((n-1)//2, -1, -1):
        shift_down(lst, i)

def heap_pop(lst):
    v = lst[0]
    sub = lst.pop()
    if len(lst) > 0:
        lst[0] = sub
        shift_down(lst, 0)
    return v

def shift_up(lst, start):
    i, j = start, (start - 1) // 2
    v = lst[start]
    while j >= 0:
        if lst[j] <= v: break
        lst[i] = lst[j]
        i, j = j, (j - 1) // 2
    lst[i] = v

def heap_push(lst, x):
    lst.append(x)
    shift_up(lst, len(lst) - 1)

