#!/usr/bin/env python

def bubble_sort(lst):
    times = len(lst)
    while times > 0:
        for i in range(times - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        times -= 1

if __name__ == '__main__':
    test_data = [2,5,3,4,1,3,6,8,7]
    bubble_sort(test_data)
    print(test_data)