# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_map = {val:i for i,val in enumerate(postorder)}

        def helper(pre_s, pre_e, post_s, post_e):
            if pre_s > pre_e:
                return None
            
            root = TreeNode(preorder[pre_s])

            if pre_s == pre_e:
                return root
            
            left_node = preorder[pre_s + 1]

            left_idx = post_map[left_node]

            left_size = left_idx - post_s + 1

            root.left = helper(
                pre_s + 1,
                pre_s + left_size,
                post_s,
                left_idx
            )

            root.right = helper(
                pre_s + left_size + 1,
                pre_e,
                left_idx + 1,
                post_e - 1
            )

            return root

        return helper(0, len(preorder)-1, 0, len(postorder)-1)

