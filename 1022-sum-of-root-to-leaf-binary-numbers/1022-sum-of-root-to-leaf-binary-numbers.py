# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # ans = 0

        # path = []

        # def helper(node):
        #     nonlocal ans
            
        #     path.append(str(node.val))
        #     if not node.left and not node.right:
        #         value = "".join(path)
        #         ans += int(value,2)
        #         path.pop()
        #         return
            
        #     if node.left:
        #         helper(node.left)
            
        #     if node.right:
        #         helper(node.right)
            
        #     path.pop()
        
        # helper(root)
        # return ans

        def helper(node, cur):
            if not node:
                return 0

            cur = cur * 2 + node.val
            
            if not node.left and not node.right:
                return cur
            
            return helper(node.left, cur) + helper(node.right, cur)
        
        return helper(root, 0)



