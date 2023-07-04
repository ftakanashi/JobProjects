#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        ans = set()

        def dfs(node):
            if node is None: return

            if node.val in to_delete:
                if node in ans: ans.remove(node)
                if node.left: ans.add(node.left)
                if node.right: ans.add(node.right)

            if node.left:
                tmp = node.left
                if node.left.val in to_delete:
                    node.left = None
                dfs(tmp)

            if node.right:
                tmp = node.right
                if node.right.val in to_delete:
                    node.right = None
                dfs(tmp)

        ans.add(root)
        dfs(root)

        return list(ans)


from typing import Optional
from collections import deque
class Solution2:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        queue = deque()
        to_delete = set(to_delete)
        ans = []
        queue.append((root, root.val in to_delete, True))
        while queue:
            node, del_flag, is_root = queue.popleft()
            l, r = node.left, node.right
            if l is not None:
                if l.val in to_delete:
                    queue.append((node.left, True, False))
                    node.left = None
                else:
                    queue.append((node.left, False, del_flag))
            if r is not None:
                if r.val in to_delete:
                    queue.append((node.right, True, False))
                    node.right = None
                else:
                    queue.append((node.right, False, del_flag))
            if not del_flag and is_root:
                ans.append(node)

        return ans