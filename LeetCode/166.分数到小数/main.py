#!/usr/bin/env python

class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0: return "0"
        minus = (n < 0) ^ (d < 0)
        n, d = abs(n), abs(d)
        i = n // d    # 整数部分
        n = n % d    # 剩余需要取小数部分

        res = str(i) if n == 0 else str(i) + '.'
        seen_nums = {}    # 一个哈希表用来记录可能出现的循环
        while n > 0:

            while n < d:    # 借位
                n *= 10
                res += '0'    # 借位k次就要加上k-1个零
            res = res[:-1]

            if n in seen_nums:    # 发现循环
                res = res[:seen_nums[n]-1] + '(' + res[seen_nums[n]-1:] + ')'
                break

            digit = n // d    # 计算一位
            res += str(digit)
            seen_nums[n] = len(res)     # 为了后面可能发生的循环进行位置记录
            n = n - digit * d

        return '-' + res if minus else res

        # minus = (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0)
        # numerator, denominator = abs(numerator), abs(denominator)

        # inte = numerator // denominator
        # if inte * denominator == numerator: return '-' + str(inte) if minus else str(inte)
        # numerator -= inte * denominator
        # res = str(inte) + '.'

        # zero_count = 0
        # while numerator < denominator:
        #     numerator *= 10
        #     zero_count += 1
        # res += '0' * (zero_count-1)

        # seen_num = []
        # prefix_len = len(res)
        # while numerator > 0:

        #     zero_count = 0
        #     while numerator < denominator:
        #         numerator *= 10
        #         zero_count += 1
        #     res += '0' * (zero_count-1)

        #     if numerator in seen_num:
        #         offset = seen_num.index(numerator)
        #         res = res[:prefix_len+offset] + '(' + res[prefix_len+offset:] + ')'
        #         break
        #     seen_num.append(numerator)
        #     digit = numerator // denominator
        #     res += str(digit)
        #     numerator -= denominator * digit

        # return '-' + res if minus else res