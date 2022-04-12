#!/usr/bin/env python
from typing import List

class SegmentTreeInArray:
    '''
    线段树类：基于数组作为底层的实现
    '''
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.seg = [0 for _ in range(self.n * 4)]
        self._build(0, 0, self.n - 1)    # 递归入口：根节点填入对应整个原数组的值

    def _build(self, node, s, e):
        '''
        输入线段树某个节点以及其对应原数组中的哪个区间([s,e])，在线段树中将该节点的值求出并填入
        '''
        if s == e:
            self.seg[node] = self.nums[s]
            return self.seg[node]
        m = (s + e) // 2
        self.seg[node] = self._build(node * 2 + 1, s, m) + self._build(node * 2 + 2, m + 1, e)
        return self.seg[node]

    def change(self, index, val, node, s, e):
        '''
        将原数组的某个指定下标index的值修改为新值val
        '''
        if s == e:
            self.seg[node] = val
            return
        m = (s + e) // 2
        if index <= m:
            self.change(index, val, node * 2 + 1, s, m)
        else:
            self.change(index, val, node * 2 + 2, m+1, e)
        self.seg[node] = self.seg[node * 2 + 1] + self.seg[node * 2 + 2]

    def getRange(self, left, right, node, s, e):
        '''
        获取原数组某个指定范围内的值
        '''
        if left == s and right == e:
            return self.seg[node]
        m = (s + e) // 2
        if right <= m:
            return self.getRange(left, right, node * 2 + 1, s, m)
        elif left > m:
            return self.getRange(left, right, node * 2 + 2, m+1, e)
        else:
            return self.getRange(left, m, node * 2 + 1, s, m) + self.getRange(m+1, right, node * 2 + 2, m+1, e)

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = SegmentTreeInArray(nums)    # 有了线段树之后题目要求的两个操作就是线段树自身的基本操作了

    def update(self, index: int, val: int) -> None:
        self.tree.change(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.getRange(left, right, 0, 0, self.n - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# 0 1 4 9