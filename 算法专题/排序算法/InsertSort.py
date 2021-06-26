#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
[<<<<<<<] [i] [未排序序列]
'''

def InsertSort(lst):
    for i in range(1, len(lst)):
        x = lst[i]    # tmp record
        j = i
        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    InsertSort(test_data)
    print(test_data)