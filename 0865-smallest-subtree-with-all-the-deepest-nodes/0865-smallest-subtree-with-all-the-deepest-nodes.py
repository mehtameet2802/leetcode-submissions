# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return 0, None
            
            dl, left = helper(node.left)
            dr, right = helper(node.right)

            if dl == dr:
                return dl + 1, node
            
            elif dl > dr:
                return dl + 1, left
            
            else:
                return dr + 1, right
            
        return helper(root)[1]
