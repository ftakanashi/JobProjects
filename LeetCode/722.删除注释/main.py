#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import re
class Solution1:
    def removeComments(self, source: List[str]) -> List[str]:
        content = "\n".join(source)
        content = re.sub("//.*|/\*(.|\n)*?\*/", "", content)
        return [l for l in content.split("\n") if len(l) > 0]

class Solution2:
    def removeComments(self, source: List[str]) -> List[str]:
        in_comment = False
        ans = []
        new_line = []
        for line in source:
            i = 0
            while i < len(line):
                if in_comment:
                    if i + 1 < len(line) and line[i:i + 2] == "*/":
                        in_comment = False
                        i += 1
                else:
                    if i + 1 < len(line) and line[i:i + 2] == "/*":
                        in_comment = True
                        i += 1
                    elif i + 1 < len(line) and line[i:i + 2] == "//":
                        break
                    else:
                        new_line.append(line[i])
                i += 1

            if not in_comment and len(new_line) > 0:
                ans.append("".join(new_line))
                new_line = []

        return ans