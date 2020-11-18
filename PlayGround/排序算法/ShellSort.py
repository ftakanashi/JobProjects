#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
|_o___|_o___|_o___|_o___|

不断缩小gap。同一个gap下，保证所有group内相隔gap的各个元素是**相对**有序的。
'''

def ShellSort(lst):
    gap = int(len(lst) // 2)
    while gap > 0:
        i = gap
        while i < len(lst):
            j = i
            while j - gap >= 0:    # 这个循环不是为了group内排序！只是为了group内相对有序调整位置
                if lst[j - gap] > lst[j]:
                    lst[j - gap], lst[j] = lst[j], lst[j - gap]
                j -= gap
            i += 1
        gap = int(gap // 2)

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    ShellSort(test_data)
    print(test_data)