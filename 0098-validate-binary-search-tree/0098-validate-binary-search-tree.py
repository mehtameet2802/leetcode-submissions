# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def helper(node, left, right):
            if not node:
                return True

            if left >= node.val or right <= node.val:
                return False
            
            left = helper(node.left, left, node.val)
            right = helper(node.right, node.val, right)

            return left and right and True
        
        return helper(root, -float('inf'), float('inf'))