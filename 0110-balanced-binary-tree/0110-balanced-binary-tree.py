# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        def helper(node):
            if not node:
                return 0, True

            left_d, left_ans = helper(node.left)
            right_d, right_ans = helper(node.right)

            if not left_ans or not right_ans:
                return 0, False

            if abs(left_d - right_d) > 1:
                return 0, False
            
            return max(left_d,right_d)+1, True
        
        return helper(root)[1]