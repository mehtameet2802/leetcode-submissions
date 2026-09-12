# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        What exactly does helper(node) return?
        What are the base cases?
        What does a non-null left result mean?
        What does a non-null right result mean?
        When should the current node be returned?
        How should p and q be compared with a node?
        Invariant:
        Expected TC and SC:
        '''

        def helper(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = helper(node.left)
            right = helper(node.right)

            if not left and not right:
                return None

            if left and right:
                return node
            
            return left or right
        
        return helper(root)