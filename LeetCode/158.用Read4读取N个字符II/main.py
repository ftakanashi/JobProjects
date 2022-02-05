#!/usr/bin/env python
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
from typing import  List

from collections import deque

def read4(buf4: List[str]) -> int:
    '''
    为了syntax检查不出错的dummy函数
    '''
    return 0

class Solution:
    def __init__(self):
        self.cache = deque()    # 声明一个缓存队列

    def read(self, buf: List[str], n: int) -> int:
        # 每次调用read时先清空buf
        # 为了能尽量贴合题意，从前向后扫描buf，将所有非空的字符置空
        for i, ch in enumerate(buf):
            if ch == "": break
            buf[i] = ""

        # 先检查缓存中是否还有剩余的字符，若有就读取
        total = 0    # 总读取字符数，同时也是buf有效区域的下标边界
        while self.cache and total < n:    # 别忘了 total < n 这个限制
            buf[total] = self.cache.popleft()
            total += 1
        # 上面这个循环，如果是self.cache为空跳出，说明此时缓存用完但是仍没有读够n个字符，所以下面继续去读取
        # 如果是total == n跳出，说明缓存中字符数就已经够满足要求的n个字符，因此下面的循环也不会进了

        while total < n:    # 继续读取
            tmp = ['' for _ in range(4)]    # 声明buf4，用于调用read4
            read_cnt = read4(tmp)
            # 此时tmp中已经有内容，且有效的是前read_cnt个字符
            # 注意如果文件读完，即read_cnt为0时，虽然此时也可直接break掉，但是下面的代码也对这点做出了限制，所以没必要提前跳出，可以等下面的break
            i = 0
            while total < n and i < read_cnt:
                buf[total] = tmp[i]    # 进行本次read4读取内容的buf写入
                total += 1
                i += 1
            # 上述循环如果是total == n跳出，那么说明本次read4读取出的字符中，只要取用前面的若干个就满足了n个字符的要求
            # 但是剩下读出来的字符又不能重新塞回文件，所以将这些字符塞入缓存队列，以供后续调用使用
            while i < read_cnt:
                self.cache.append(tmp[i])
                i += 1

            # 至此，一次read4调用以及相关后续处理完成了。如果此时total == n，那么循环很快就会跳出
            # elif 此时read_cnt == 4，说明一来n个字符还未满足，二来文件也还没读完，那么直接下轮循环
            # 唯独尚未考虑的是read_cnt < 4的情况，此时文件已经读完，那么不管n个字符是否已经满足，都应该跳出循环了
            if read_cnt < 4:
                break

        return total