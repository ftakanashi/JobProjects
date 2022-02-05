#!/usr/bin/env python
from typing import List

class Solution:
    def help(self, wordsDict: List[str], word1: str, word2: str) -> int:
        '''
        LC.243的代码直接copy过来
        '''
        pa = pb = float('-inf')
        ans = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                pa = i
                ans = min(ans, pa - pb)
            elif word == word2:
                pb = i
                ans = min(ans, pb - pa)
        return ans

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 != word2:
            return self.help(wordsDict, word1, word2)
        else:
            indices = [float('-inf')] + [i for i in range(len(wordsDict)) if wordsDict[i] == word1]
            # return min(map(lambda i: indices[i]-indices[i-1], range(1, len(indices))))    # 炫酷的一行写法
            ans = float('inf')
            for i in range(1, len(indices)):
                ans = min(ans, indices[i] - indices[i-1])
            return ans