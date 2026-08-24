# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        moves = 0
        def helper(node):
            nonlocal moves

            if not node:
                return 0
            

            left = helper(node.left)
            right = helper(node.right)

            moves += abs(left)
            moves += abs(right)

            bal = node.val + left + right - 1

            return bal

        helper(root)
        return moves
            