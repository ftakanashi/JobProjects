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


def iter_quick_sort(lst):
    '''
    最近面试中也开始常考迭代形式的快排了。
    基于递归形式的快排，只需要稍稍改动就可以变成迭代形式。
    递归转迭代，本质上就是手动将递归栈给模拟出来就好了
    '''
    n = len(lst)

    def partition(left, right):
        '''
        和递归形式的partition函数的区别在
        1. 因为不是递归，不用设置递归结束条件
        2. 交换完本趟后不递归处理两侧，而是直接返回pivot值当前的坐标
        '''
        pivot = lst[left]
        i = j = left + 1
        while j <= right:
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
            j += 1
        i -= 1
        lst[left], lst[i] = lst[i], lst[left]
        return i

    stack = [n-1, 0]
    while stack:
        l = stack.pop()
        r = stack.pop()
        if l >= r: continue # 如果l >= r，就无需进入，相当于递归时的递归终止条件

        pivot_i = partition(l, r)    # 进行一趟交换

        # 下面是将要处理的两侧分别入栈。注意因为是栈，所以要倒着入。
        stack.append(pivot_i - 1)
        stack.append(l)
        stack.append(r)
        stack.append(pivot_i + 1)


if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    QuickSort(test_data)
    print(test_data)