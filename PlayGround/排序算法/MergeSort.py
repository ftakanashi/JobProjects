#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    归并排序：
    思想很简单，首先也是基于递归的分治。
    先深入到最小的单元，即长度为1的子列表。然后层层向上，合并相邻的两个子列表。
    合并过程中进行大小的比较以及合并操作，保证每个子列表内部都是有序的。
    最终合并成原长度的原列表后，原列表也是有序的。

    关于归并排序的一点分析。
    首先，为了方便计算，假设列表长度为n = 2^k。
    此时归并排序用到的额外空间，从最底层的长度为1的子列表开始算起，一层层向上叠加，是 2^k + 2^(k-1) + ... + 2^2 + 2^1 + 2^0 。
    这是一个等比数列，套用求和公式得到其和是 2^(k+1) - 1，即 2*n - 1。
    所以空间复杂度是O(n)。

    时间复杂度，首先结论是，不能论最好还是最坏都是O(nlogn)，和快排基本一样。
    归并排序的时间复杂度计算可以盯着"比较次数"算，因为每比较一次就意味着要append一次。
    然后记住一个结论，当两个长度为x的数组为了归并进行比较，最多的比较次数是 2x - 1，最少的比较次数是x。
    这样，就可以推算了。最好情况下，长度为n = 2^k数组进行归并排序，其比较次数按照层级来算分别是：
    2^(k-1) * 2^0    # 最底层进行2^(k-1)对子列表之间的比较，且每对只比较一次，以此类推
    2^(k-2) * 2^1
    ...
    2^0 * 2^(k-1)
    加和起来是，2^(k-1) * (k - 1)，其中n = 2^k而k = log2(n)。所以这个式子等于 (n/2) * (log2(n) - 1)。整体是O(nlogn)

    另一方面，如果是按最差情况算。其比较次数按层级来算分别是：
    2^(k-1) * [ 2*(2^0) - 1 ]
    2^(k-2) * [ 2*(2^1) - 1 ]
    ...
    2^0 * [ 2*(2^(k-1)) - 1 ]
    求和后得到，2^K * k - 2^k + 1。代入n = 2^k，相当于是 n * log2(n) - n + 1。所以也是O(nlogn)
'''

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
    m, n = len(left) - 1, len(right) - 1
    while i <= m and j <= n:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i <= m: res.extend(left[i:])
    if j <= n: res.extend(right[j:])

    return res


# 另一种形式的归并排序，在原数组上in-place地逐渐更新数据
def MergeSort2(lst):

    def recursive_sort(lst, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        recursive_sort(lst, left, mid)
        recursive_sort(lst, mid + 1, right)

        # merge the lists
        res = []
        i, j = left, mid + 1
        m, n = mid, right
        while i <= m and j <= n:
            if lst[i] <= lst[j]:
                res.append(lst[i])
                i += 1
            else:
                res.append(lst[j])
                j += 1
        while i <= m:
            res.append(lst[i])
            i += 1
        while j <= n:
            res.append(lst[j])
            j += 1
        lst[left : right + 1] = res

    recursive_sort(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    sorted_test_data = MergeSort(test_data)
    print(sorted_test_data)
    test_data = [2,5,3,4,1,3,6,8,7,4,6,7,33,4,6,8,2,12]
    MergeSort2(test_data)
    print(test_data)