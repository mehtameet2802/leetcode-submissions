"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        '''
        Pattern:
        - N-ary Tree
        - DFS
        - Recursion

        TC - O(N)
        SC - O(H)

        Balanced → O(log_K N)
        Worst case → O(N)

        Optimal → Yes
        '''
        
        def helper(root):
            if not root:
                return 0
            
            d = 0
            for child in root.children:
                d = max(d, helper(child))
            
            return d + 1
        
        return helper(root)