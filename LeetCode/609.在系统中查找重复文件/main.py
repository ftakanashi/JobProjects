#!/usr/bin/env python
from typing import List

from collections import defaultdict

import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        con2path = defaultdict(list)
        for path in paths:
            dirpath, *files = path.strip().split()    # 这个技巧别忘了
            for fileinfo in files:
                match = re.search("^(.+?)\((.+?)\)$", fileinfo)
                filename = match.group(1)
                content = match.group(2)
                con2path[content].append(f"{dirpath}/{filename}")

        ans = []
        for content in con2path:
            if len(con2path[content]) <= 1: continue
            ans.append(con2path[content])
        return ans