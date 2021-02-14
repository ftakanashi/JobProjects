#!/usr/bin/env python

import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None: return ''
        seq = []
        queue = collections.deque([])
        queue.append(root)
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                seq.append('null' if node is None else str(node.val))
                if node is not None:
                    queue.append(node.left), queue.append(node.right)

        return ','.join(seq)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return
        data = data.split(',')
        queue = collections.deque([])
        orig_root = TreeNode(data[0])
        queue.append(orig_root)
        i = 1
        while i < len(data):
            node = queue.popleft()
            l_val, r_val = data[i], data[i+1]
            if l_val is not None:
                node.left = TreeNode(l_val)
                queue.append(node.left)
            if r_val is not None:
                node.right = TreeNode(r_val)
                queue.append(node.right)
            i += 2
        return orig_root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))