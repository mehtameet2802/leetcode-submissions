# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return 

            if low <= node.val <= high:
                ans += node.val

            if node.val < high:
                helper(node.right)
            
            if node.val > low:
                helper(node.left)
        
        helper(root)
        return ans
