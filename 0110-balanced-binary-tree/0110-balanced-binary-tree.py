# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return True, 0
            
            lr, ld = helper(node.left)
            rr, rd = helper(node.right)
            
            if not lr or not rr:
                return False, 0
            
            if abs(ld-rd) <= 1:
                return True, max(ld,rd) + 1 
            
            return False, 0

        return helper(root)[0]
            
