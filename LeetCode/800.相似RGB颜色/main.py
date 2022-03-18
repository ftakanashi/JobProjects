#!/usr/bin/env python

import bisect
class Solution:
    def similarRGB(self, color: str) -> str:
        color_strs = ["00", "11", "22", "33", "44", "55", "66", "77",
                      "88", "99", "aa", "bb", "cc", "dd", "ee", "ff"]
        colors = [int(c, 16) for c in color_strs]

        r, g, b = color[1:3], color[3:5], color[5:7]
        ans = "#"
        for c in [r, g, b]:
            num = int(c, 16)
            pos = bisect.bisect_left(colors, num)
            if abs(colors[pos] - num) <= abs(colors[pos - 1] - num):
                ans += color_strs[pos]
            else:
                ans += color_strs[pos-1]
        return ans