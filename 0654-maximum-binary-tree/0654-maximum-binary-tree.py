# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nums_map = { val:i for i,val in enumerate(nums) }

        def build(l, r):
            if l>r:
                return None
            max_i = nums_map[max(nums[l:r+1])]

            node = TreeNode(nums[max_i])
            node.left = build(l, max_i-1)
            node.right = build(max_i+1, r)

            return node
        
        return build(0, len(nums)-1)
