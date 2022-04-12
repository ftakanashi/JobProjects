#!/usr/bin/env python
from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = row_width = 0
        for i, ch in enumerate(s):
            ch_width = widths[ord(ch) - ord('a')]
            if 100 - row_width < ch_width:
                row += 1
                row_width = 0
            row_width += ch_width

        return [row + 1, row_width]