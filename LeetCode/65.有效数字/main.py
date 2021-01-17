#!/usr/bin/env python
from typing import List

import collections
class Solution1:
    def checkFig(self, s: str, form: str) -> bool:

        # 最开始直接去除符号的影响。因为符号只能出现在第一位，如果后面再出现就是不合法的。
        if len(s) > 0 and s[0] in '+-':
            s = s[1:]
            if len(s) > 0 and s[0] in '+-': return False
        if len(s) == 0: return False

        # 判断字符串是否是合法的整数，即各个位置是否都是数字即可。
        if form == 'int':
            for ch in s:
                if ch not in '1234567890':
                    return False

        # 判断字符串是否是合法的浮点数
        # 这里除了简单的字符check，还有对于小数点的判断。如果小数点多于一个或者s == '.'是False
        # 其他情况都没问题
        elif form == 'float':
            counter = collections.Counter(s)
            if counter['.'] > 1 or s == '.': return False
            for i, ch in enumerate(s):
                if ch not in '1234567890.':
                    return False

        return True

    def isNumber(self, s: str) -> bool:
        s = s.lower()    # 由于e和E是同一个意思，为了简洁，直接lower掉

        # 基本字符检查
        for ch in s:
            if ch not in set(list('1234567890e+-.')):
                return False

        # 构建counter
        counter = collections.Counter(s)

        # 判断是否含有e
        if counter['e'] > 0:
            if counter['e'] > 1: return False    # 含有一个以上的e肯定是不行
            a, b = s.split('e')    # 此时a可以是浮点或者整数，b必须是整数
            flag = self.checkFig(a, 'float') and self.checkFig(b, 'int')
        else:
            flag = self.checkFig(s, 'float')

        return flag

class Solution2:
    def isNumber(self, s: str) -> bool:
        finals = [0,0,0,1,0,1,1,0,1]
        transfer = [[ 0, 1, 6, 2,-1,-1],
                    [-1,-1, 6, 2,-1,-1],
                    [-1,-1, 3,-1,-1,-1],
                    [ 8,-1, 3,-1, 4,-1],
                    [-1, 7, 5,-1,-1,-1],
                    [ 8,-1, 5,-1,-1,-1],
                    [ 8,-1, 6, 3, 4,-1],
                    [-1,-1, 5,-1,-1,-1],
                    [ 8,-1,-1,-1,-1,-1]]
        state = 0
        char_map = {
            ' ': 0,
            '+': 1,
            '-': 1,
            '.': 3,
            'e': 4,
            'E': 4,
        }
        for i, ch in enumerate(s):
            if ch in '1234567890':
                to_state = 2
            elif ch in char_map:
                to_state = char_map[ch]
            else:
                to_state = 5
            state = transfer[state][to_state]
            if state < 0:
                return False

        return finals[state] == 1