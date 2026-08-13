# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None

        cur_f = 0
        max_f = 0

        ans = []

        def helper(node):
            nonlocal ans
            nonlocal prev
            nonlocal max_f
            nonlocal cur_f

            if not node:
                return

            helper(node.left)
            
            if prev is None:
                prev = node.val
                cur_f = 1
                ans = [node.val]
            elif prev == node.val:
                cur_f += 1
            else:
                if cur_f == max_f:
                    ans.append(prev)
                elif cur_f > max_f:
                    ans = [prev]
                    max_f = cur_f
                
                prev = node.val
                cur_f = 1

            helper(node.right)

        helper(root)

        if cur_f == max_f:
            ans.append(prev)
        elif cur_f > max_f:
            ans = [prev]
            max_f = cur_f

        return ans 

