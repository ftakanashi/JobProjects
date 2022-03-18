#!/usr/bin/env python
from typing import List

from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nums = deque(nums)    # 将nums队列化方便后续处理
        root = TreeNode(nums.popleft() % 10)
        layer = 2
        prev = [root, ]
        while nums:
            curr = []    # 从左到右，带null地收集本层节点
            while nums and layer == nums[0] // 100:    # 遍历本层所有节点，即所有百位数和layer值一致的num
                num = nums.popleft()
                pos, val = num // 10 % 10, num % 10
                node = TreeNode(val)
                while len(curr) < (pos - 1):    # 用None补齐，保证子节点可以正确地找到node在curr中的坐标
                    curr.append(None)
                curr.append(node)
                if pos & 1 == 1:    # 通过pos的奇偶性可以知道其实父节点的左子还是右子节点
                    prev[(pos-1)//2].left = node
                else:
                    prev[(pos-1)//2].right = node
            prev = curr
            layer += 1

        # 下面就是求路径和的DFS，就不多说啦
        ans = 0
        def dfs(node, path):
            nonlocal ans
            if node.left is None and node.right is None:
                path += node.val
                ans += path
                return
            if node.left is not None:
                dfs(node.left, path + node.val)
            if node.right is not None:
                dfs(node.right, path + node.val)
        dfs(root, 0)
        return ans