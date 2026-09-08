# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        What does helper/node state represent? - the helper function when called on any node tells us if the node is valid or not, if valid then bydefault all its child nodes and child sub trees also become valid and vice versa

        What condition makes a node valid? - the left subtree of the node must be valid and the right subtree of the node must be valid, along with the curretn node being valid
        validity conditions - 
        The left subtree of a node contains only nodes with keys strictly less than the node's key.The right subtree of a node contains only nodes with keys strictly greater than the node's key.

        What must be true for every node in its left and right subtree? - all the values of the nodes in left subtree must be less than node's value and all the values for nodes in right subtree must be greater than node's value.

        also if propogation is happening from the root node then we will have to pass limits such that both left and right nodes values are within their respective limits

        TC - o(n)
        sc - O(h), h is n or log n

        '''

        def helper(node,left,right):
            if not node:
                return True
            
            if left < node.val < right:
                return helper(node.left,left,node.val) and helper(node.right,node.val,right)

            return False

        inf = float('inf')
        return helper(root, -inf, inf)