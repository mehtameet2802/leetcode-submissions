# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(root, cur):
            nonlocal targetSum

            if not root:
                return False

            cur = cur + root.val

            if not root.left and not root.right and cur == targetSum:
                return True
            
            left = helper(root.left, cur)
            right = helper(root.right, cur)

            return left or right

        
        return helper(root, 0)