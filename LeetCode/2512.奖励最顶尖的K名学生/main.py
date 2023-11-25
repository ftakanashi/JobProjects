#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        feedback = {}
        for w in positive_feedback: feedback[w] = 3
        for w in negative_feedback: feedback[w] = -1
        scores = []
        for _id, rep in zip(student_id, report):
            score = sum(feedback.get(w, 0) for w in rep.split())
            heapq.heappush(scores, (-score, _id))

        ans = []
        for _ in range(k):
            _, _id = heapq.heappop(scores)
            ans.append(_id)
        return ans