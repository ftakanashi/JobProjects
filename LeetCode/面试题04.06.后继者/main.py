#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            if node is None: return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)

        l, r = 0, len(nodes) - 1
        while l <= r:
            mid = (l + r) // 2
            if nodes[mid].val <= p.val:
                l = mid + 1
            else:
                r = mid - 1
        return nodes[l] if l < len(nodes) else None

class Solution2:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        node = root
        parents = {root: None}
        while node and node is not p:    # 定位节点p且保存根节点到p的遍历路径
            if p.val < node.val:
                parents[node.left] = node
                node = node.left
            elif p.val > node.val:
                parents[node.right] = node
                node = node.right
            else:
                break

        if node is None: return    # 当树中没有p的情况

        if node.right:    # p本身就有右子树的情况
            ans = node.right
            while ans.left:
                ans = ans.left
        else:    # p没有右子树的情况
            ans = parents[node]
            while ans and ans.val < node.val:
                ans = parents[ans]
        return ans