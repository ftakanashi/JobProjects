#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
基数排序
针对待排序对象全是自然数的一种桶排序实现。

从个位开始向数组中存在的最高位依次进行处理。
每个位处理时，创建位的值是0-9的10个桶。依次按照位值把原数放入桶中，然后重排。

得到重排的序列后，继续向更高一位做同样的处理。

低位处理完后要把重排得到的序列传递给下一轮高位处理的原因是，这样可以做到高位的同一个桶中数字的有序。

比如48, 35, 41这个序列。
如果直接排十位，按照十位值来说，48和41是相同的桶，由于原序列48在前，所以最终拍出来的也是48在前，变成35， 48， 41
但是如果先处理个位，得到序列41, 35, 48；而后再处理十位，此时桶4中是41， 48。即正确的顺序
'''

def RadixSort(lst):
    n = len(str(max(lst)))    # 要处理到的最大位数
    for k in range(n):
        buckets = [[] for _ in range(10)]
        for i in lst:
            i_n = (i // (10 ** k)) % 10    # 数字i的k位数（k=0个位，k=1十位……）
            buckets[i_n].append(i)
        lst = [i for bucket in buckets for i in bucket]    # 注意这个表达式，一个表达式flatten一个二维的列表

    return lst

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    new_test_data = RadixSort(test_data)
    print(test_data)
    print(new_test_data)