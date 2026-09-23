# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        
        def helper(node):
            if not node:
                return 0,0
            
            left_bal, left_moves = helper(node.left)
            right_bal, right_moves = helper(node.right)

            cur_bal = left_bal + right_bal + node.val - 1

            cur_moves = abs(left_moves) + abs(right_moves) + abs(cur_bal)
            
            return cur_bal, cur_moves
        
        return helper(root)[1]