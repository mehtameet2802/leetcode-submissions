# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        max_f = 0

        def helper(node):
            nonlocal max_f

            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            max_f = max(max_f, left + right)

            return max(left, right)
        
        helper(root)
        return max_f
