# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0

        inorder_i = {val:i for i,val in enumerate(inorder)}


        def helper(l, r):
            nonlocal inorder_i, pre_idx

            if l > r:
                return None
            
            node = TreeNode(preorder[pre_idx])
            in_idx = inorder_i[preorder[pre_idx]]
            pre_idx += 1

            node.left = helper(l, in_idx - 1)
            node.right = helper(in_idx + 1, r)

            return node
        
        return helper(0, len(inorder)-1)