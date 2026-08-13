# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pst_idx = len(postorder) - 1
        ind_map = {val:i for i,val in enumerate(inorder)}

        def helper(l, r):
            nonlocal pst_idx, ind_map

            if l > r:
                return None
            
            ind_idx = ind_map[postorder[pst_idx]]
            root_val = postorder[pst_idx]
            pst_idx -= 1

            
            node = TreeNode(root_val)
            right = helper(ind_idx + 1, r)
            left = helper(l, ind_idx - 1)

            node.left = left
            node.right = right

            return node
        
        return helper(0, len(inorder) - 1)

            

