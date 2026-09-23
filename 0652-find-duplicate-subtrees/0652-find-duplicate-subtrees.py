# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        pattern = {}
        used = set()
        ans = []

        def helper(node):
            if not node:
                return "#"
            
            left_pattern = helper(node.left)
            right_pattern = helper(node.right)

            node_pattern = str(node.val) +"-"+ left_pattern +"-"+ right_pattern

            if node_pattern in pattern and node_pattern not in used:
                ans.append(node)
                used.add(node_pattern)
            
            pattern[node_pattern] = node
            return node_pattern
        
        helper(root)
        return ans