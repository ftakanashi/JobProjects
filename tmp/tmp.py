#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

def search_start_end(q: str, i: int, cands: List[str], start: int, end: int):

    def binary_search(left, right, lower=True):
        while left <= right:
            mid = (left + right) // 2
            cand = cands[mid]
            if lower:
                if i >= len(cand) or cand[i] < q: left += 1
                else: right -= 1
            else:
                if i >= len(cand) or cand[i] <= q: left += 1
                else: right -= 1
        return left

    return [binary_search(start, end),
            binary_search(start, end, lower=False) - 1]

def keywordsSuggestions(repo: List[str], query: str) -> List[List[str]]:
    if len(query) <= 1: return []
    query = query.lower()
    prefix = query[:2]
    cands = [cand.lower() for cand in repo if cand.lower().startswith(prefix)]
    cands.sort()

    res = []
    res.append(cands[:3])
    i = 2
    start, end = 0, len(cands) - 1
    while i < len(query):
        start, end = search_start_end(query[i], i, cands, start, end)
        res.append(cands[start:end+1] if end-start <= 2 else cands[start:start+3])
        i += 1
    return res

if __name__ == '__main__':
    repo = [
        'baggage', 'bags', 'banner', 'box', 'cloths'
    ]
    query = 'bags'
    print(keywordsSuggestions(repo, query))