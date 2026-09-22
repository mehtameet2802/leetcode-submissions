# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        pre_idx = 0
        ind_map = {}

        for idx,node in enumerate(inorder):
            ind_map[node] = idx
        
        
        def helper(left, right):
            nonlocal pre_idx

            if left > right:
                return None
            
            if pre_idx >= len(preorder):
                return None

            node = TreeNode(preorder[pre_idx])
            ind_idx = ind_map[preorder[pre_idx]]

            pre_idx += 1
            node.left = helper(left, ind_idx-1)
            node.right = helper(ind_idx + 1,right)

            return node

        
        return helper(0,len(preorder)-1)
