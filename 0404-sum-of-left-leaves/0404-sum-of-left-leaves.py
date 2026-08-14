# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, isLeft):
            if not node:
                return 0
            
            if not node.left and not node.right and isLeft == 1:
                return node.val

            left = helper(node.left, 1)
            right = helper(node.right, 0)
            
            return left + right
        
        return helper(root, 0)