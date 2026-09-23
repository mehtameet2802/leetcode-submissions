# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        
        def helper(node):
            if not node:
                return 0,0
            
            left_rob, left_no_rob = helper(node.left)
            right_rob, right_no_rob = helper(node.right)

            return node.val + left_no_rob + right_no_rob, max(left_rob + right_rob, left_no_rob+right_no_rob, left_rob + right_no_rob, left_no_rob + right_rob)
        
        root_rob, root_no_rob = helper(root)
        return max(root_rob, root_no_rob)
