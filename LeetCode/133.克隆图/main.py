#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return
        orig_clone_map = {}

        def dfs(orig_node: 'Node') -> 'Node':
            if orig_node in orig_clone_map:
                return orig_clone_map[orig_node]
            clone_node = Node(val=orig_node.val)
            orig_clone_map[orig_node] = clone_node
            for nb in orig_node.neighbors:
                clone_nb = dfs(nb)
                clone_node.neighbors.append(clone_nb)
            return clone_node

        new_node = dfs(node)
        return new_node