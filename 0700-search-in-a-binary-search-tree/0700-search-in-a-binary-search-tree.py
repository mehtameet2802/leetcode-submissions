# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return None
            
            if node.val == val:
                return node
            
            left = helper(node.left)
            right = helper(node.right)

            return left or right
        
        return helper(root)

            
