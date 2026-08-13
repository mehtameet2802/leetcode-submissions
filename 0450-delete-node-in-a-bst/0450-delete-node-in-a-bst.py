# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        '''
        Pattern:
        - BST
        - Recursion
        - Search
        - Inorder Successor

        TC - O(H)
        SC - O(H)

        Balanced → O(log N)
        Worst case → O(N)

        Optimal → Yes
        '''
        
        def getNode(node):
            while node and node.left:
                node = node.left

            return node

        def delete(node, key):
            if not node:
                return None

            if node.val > key:
                node.left =  delete(node.left, key)
            elif node.val < key:
                node.right =  delete(node.right, key)
            else:
            
                if not node.left:
                    return node.right
                
                if not node.right:
                    return node.left

                new_node = getNode(node.right)

                node.val = new_node.val

                node.right = delete(node.right, new_node.val)
                
            
            return node

            
        
        return delete(root, key)