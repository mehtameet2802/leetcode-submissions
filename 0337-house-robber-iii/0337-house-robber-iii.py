# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # def helper(node):
        #     if not node:
        #         return 0
            
        #     l1 = l2 = r1 = r2 = 0

        #     if node.left:
        #         l1 = helper(node.left.left) + helper(node.left.right)
                
        #     if node.right:
        #         r1 = helper(node.right.right) + helper(node.right.left)
            
        #     l2 = helper(node.left)
        #     r2 = helper(node.right)

        #     return max(l1+r1+node.val, l2+r2)
        
        # return helper(root)


        def helper(node):
            if not node:
                return 0,0

            rob_l, skip_l = helper(node.left)
            rob_r, skip_r = helper(node.right)

            rob = node.val + skip_l + skip_r

            skip = max(rob_l, skip_l) + max(rob_r, skip_r)

            return rob, skip

        rob, skip = helper(root)

        return max(rob, skip)