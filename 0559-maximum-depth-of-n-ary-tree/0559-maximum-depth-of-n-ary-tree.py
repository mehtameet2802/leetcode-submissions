"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def helper(root):
            if not root:
                return 0
            
            d = 0
            for child in root.children:
                d = max(d, helper(child))
            
            return d + 1
        
        return helper(root)