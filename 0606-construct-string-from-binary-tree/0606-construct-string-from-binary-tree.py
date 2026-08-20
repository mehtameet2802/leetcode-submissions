# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        ans = []

        def helper(node):
            nonlocal ans

            if not node:
                return
            
            ans.append(str(node.val))

            if not node.left and not node.right:
                return

            ans.append("(")

            helper(node.left)
            ans.append(")")

            ans.append("(")
            helper(node.right)
            if ans[-1] != "(":
                ans.append(")")
            else:
                ans.pop()

        helper(root)

        return "".join(ans)

