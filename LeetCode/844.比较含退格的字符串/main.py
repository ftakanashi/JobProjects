#!/usr/bin/env python
# -*- coding:utf-8 -*-

def solution1(S, T):

    def simulation(s):
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif len(stack) > 0:    # empty_list.pop会报错
                stack.pop()
        return ''.join(stack)

    return simulation(S) == simulation(T)


def solution2(S, T):
    i = len(S) - 1
    j = len(T) - 1
    s_del_count, t_del_count = 0, 0
    new_s_char, new_t_char = None, None
    while i >= 0 or j >= 0:    # 一个扫描到头了另一个也还要继续扫描，说不定前面没有有效字符了。
        while i >= 0:
            s_c = S[i]
            if s_c == '#':
                s_del_count += 1
            elif s_del_count > 0:
                s_del_count -= 1
            else:
                new_s_char = s_c
                break
            i -= 1

        while j >= 0:
            t_c = T[j]
            if t_c == '#':
                t_del_count += 1
            elif t_del_count > 0:
                t_del_count -= 1
            else:
                new_t_char = t_c
                break
            j -= 1

        if i >= 0 and j >= 0 and new_s_char != new_t_char:
            # 有效字符是否相同比较必须保证两者都还没扫到头，要不然比较的是历史字符，没有意义
            return False
        if (i < 0)^(j < 0):
            # 运行到此处如果一方扫描到头另一方却还是没有，没有的那一方必然是又找到了新的有效字符
            # 此时只能返回False了
            return False

        i -= 1
        j -= 1

    return True

