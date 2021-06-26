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

import random
def randomized_quick_sort(lst):
    '''
    带有随机化优化的快排
    原始快排对于原本就有序的数组比如range(50000)，效率很低（O(n^2))。
    原因在于每次选择的pivot即nums[left]，都恰好是left和right间最小的数。
    现在使用随机化选择left和right中的某个pivot，避免上述情况的出现
    '''
    def randomized_partition(left, right):
        if left >= right: return

        # 添加下面两行，其余都不变即可
        rand_i = random.randint(left, right)
        lst[rand_i], lst[left] = lst[left], lst[rand_i]

        i = j = left + 1
        while j <= right:
            if lst[j] < lst[left]:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
            j += 1
        i -= 1
        lst[i], lst[left] = lst[left], lst[i]
        randomized_partition(left, i - 1)
        randomized_partition(i + 1, right)

    randomized_partition(0, len(lst) - 1)

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    QuickSort(test_data)
    print(test_data)