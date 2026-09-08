# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Required output: - diameter
        What helper(node) returns: max length of left or right, + 1
        What final answer represents: dimaeter of the tree
        Invariant: node != null
        Pseudocode:
        initiate ans = 0
        caller helper for root node
        inside the helper if node is null return 0
        call helper for node.left
        call helper for node.right
        add result of left and right (ie depth of left and right nodes), compare it with global ans to get the diameter
        compare return result of left and right, whichever depth is maximum add 1 and return it.
        outside the helper definition return the ans

        Complexity: O(n)
        '''


        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            ans = max(ans, left + right)

            return max(left,right) + 1
        
        helper(root)
        return ans