#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def dfs(node):
            if node is None: return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return " ".join([str(num) for num in res])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        postorder = [int(n) for n in data.split()]
        if len(postorder) == 0: return

        def rec(start, end):
            if start > end: return
            v = postorder[end]
            root = TreeNode(v)
            pos = end
            for i in range(start, end):    # 寻找序列中start,end-1间第一个大于postorder[end]的位置，该位置为左右子树分界线
                if postorder[i] > v:
                    pos = i
                    break
            root.left = rec(start, pos - 1)
            root.right = rec(pos, end - 1)
            return root

        return rec(0, len(postorder) - 1)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans