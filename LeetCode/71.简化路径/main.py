#!/usr/bin/env python
from typing import List

import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub('/+', '/', path)
        stack = []
        for p in path.strip('/').split('/'):
            if p == '.':
                pass
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        res = '/'
        res += '/'.join(stack)

        return res