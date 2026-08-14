# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return -1, 0, 0
            
            left_max, left_left, left_right = helper(node.left)
            right_max, right_left, right_right = helper(node.right)

            left = left_right + 1
            right = right_left + 1

            best = max(left_max, right_max, left_right, right_left)

            return best, left, right

        return helper(root)[0]
            
            