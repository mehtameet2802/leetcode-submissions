# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        What does helper(node) return? - it returns none or LCA node, which can be p or q itself 
        When does a node return itself? - when itself is p or q
        When do both child calls returning non-null prove the answer is node? - it means both the childs are p and q and hence current node is LCA so return current node

        pseudocode - 
        def helper
            if not node return None
            if node == p or node == q:
                return node

            left = helper(node.left)
            right = helper(node.right)

            if left == p and right == q:
                return node
            if right == q and left == p:
                return node

            if left == p  or left == q:
                return left
            
            if right == p or right == q:
                return right
        
        return helper(root)

        Complexity - TC - O(n), SC - O(h) h is n, log n
        '''

        def helper(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                return node
            
            return left or right

        return helper(root)