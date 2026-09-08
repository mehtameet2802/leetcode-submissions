# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        '''
        Pattern prediction:

        Required output: Max product of splitted sums

        What information must be known before considering a cut? - what 2 sums will be available if split is made and what will be the product, if the product greater than current max product or not

        What helper(node) should return: for each node it should return the sum of left, right and current node, which will be utilized to calculate in parent node what possible sums and product can be achieved if we split left tree or right tree and also if we split then will we get max product or not

        What global value, if any, is needed: global value of ans as the max product will be required

        Invariant: if the node is null return 0, if not null then get left node sum, right node sum an determine split possible and what value is achieved add both sums to root node value and return

        Pseudocode:
        ans - a global var
        total - a global var
        iterate through the tree and calculate the total sum of all the node
        def helper func takes node
        in helper - 
            if not node return 0
            call helper for node.left
            call helepr for node.right
            based on sums returned for left and right children determine which to split based on max products that can be achieved, update the ans with max product
            reuturn sum of left child, right childe and node.val
        call helper with root node
        return ans

        Complexity: TC - O(n), SC - O(h), h being log n or n
        '''

        ans = 0
        total = 0
        MOD = pow(10,9) + 7

        def get_total(node):
            nonlocal total

            if not node:
                return
            
            total += node.val
            get_total(node.left)
            get_total(node.right)

        def helper(node):
            nonlocal ans

            if not node:
                return 0
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)

            max_prod = max(right_sum*(total-right_sum), left_sum*(total-left_sum))
            ans = max(ans, max_prod)

            return node.val + left_sum + right_sum

        get_total(root)
        helper(root)
        return ans%MOD