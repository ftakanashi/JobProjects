#!/usr/bin/env python
class Solution:

    def analyze(self, num: int) -> str:
        '''
        将一个[0,999]的数字转化成题目要求的字符串形式
        '''
        one_map = [    # 一位数的映射（为了方便前面加了Zero
            'Zero', 'One', 'Two', 'Three', 'Four', 'Five',
            'Six', 'Seven', 'Eight', 'Nine', 'Ten'
        ]
        two_map = [    # [11,19]的映射（为了方便加了前面加了Ten
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        ten_map = [    # 10的整数倍的映射
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        res = []
        if num >= 100:
            res.append(one_map[num // 100])
            res.append('Hundred')
            res.extend(self.analyze(num % 100))    # 递归处理
        elif num >= 20:    # 比较一般的情况，当然10的倍数在这里也考虑了
            res.append(ten_map[num // 10])
            if num % 10 != 0:
                res.append(one_map[num % 10])
        elif num >= 10:    # 11-19的情况
            res.append(two_map[num - 10])
        elif num > 0:    # 一位数的情况
            res.append(one_map[num])
        else:    # 这里其实就是指num == 0了，虽说返回Zero可以有机结合到上面代码中，但是为了配合外层加后缀，这里选择不返回任何东西
            pass

        return res

    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'    # 特殊情况处理。虽说Zero可以整合到下面的流程中，但是会让代码很复杂
        s = ''
        suf_map = ['', 'Thousand', 'Million', 'Billion']    # 后缀集合
        i = 0
        while num > 0:
            part = self.analyze(num % 1000)
            if len(part) > 0:    # 注意这行，若part是空，说明 num % 1000 == 0，此时不需要加任何后缀，因此直接跳过下面扩充s的过程
                s = ' '.join(part) + ' ' + suf_map[i] + ' ' + s
            num = num // 1000
            i += 1
        return s.strip()    # 最后有可能有空格，也懒得改上面代码了，直接这里strip掉