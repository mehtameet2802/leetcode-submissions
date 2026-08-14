# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def helper(node, parent, grandParent):
            if not node:
                return 0
            
            cur = 0
            if grandParent and grandParent % 2 == 0:
                cur += node.val
            
            left = helper(node.left, node.val, parent)
            right = helper(node.right, node.val, parent)

            return cur + left + right
        
        return helper(root, None, None)