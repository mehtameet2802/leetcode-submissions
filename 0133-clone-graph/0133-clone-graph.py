"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        TC - O(V)

        Auxiliary space:
            seen       → O(V)
            recursion  → O(V) worst case
            --------------------
            total      → O(V)

        Output:
            cloned graph → O(V + E)
        '''
        seen = {}
        
        def helper(node):
            if not node:
                return None

            if node in seen:
                return seen[node]

            new_node = Node(node.val)
            seen[node] = new_node

            for neighbour in node.neighbors:
                new_node.neighbors.append(helper(neighbour))

            return new_node
        
        return helper(node)