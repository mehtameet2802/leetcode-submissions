# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # def getLCA(node):
        #     if not node:
        #         return None
            
        #     if node.val == startValue or node.val == destValue:
        #         return node
            
        #     left = getLCA(node.left)
        #     right = getLCA(node.right)

        #     if left and right:
        #         return node
            
        #     if left:
        #         return left
            
        #     return right


        # def dfs(node, value):
        #     if not node:
        #         return "", False

        #     if node.val == value:
        #         return "", True
            
        #     d1, left = dfs(node.left, value)
        #     d2, right = dfs(node.right, value)

        #     if left:
        #         state = "L"+d1
        #         return state, True
            
        #     if right:
        #         state = "R"+d2
        #         return state, True
            
        #     return "", False
            
        
        # lca = getLCA(root)

        # ans = ""
        # if lca.val == startValue:
        #     ans, _ = dfs(lca, destValue)
        
        # elif lca.val == destValue:
        #     ans, _ = dfs(lca, startValue)
        #     ans = "U"*len(ans)

        # else:
        #     ans1, _ = dfs(lca, startValue)
        #     ans2, _ = dfs(lca, destValue)

        #     ans1 = "U"*len(ans1)
        #     ans = ans1+ans2

        # return ans


        start_path = []
        end_path = []
        path = []

        def helper(node):

            if not node:
                return

            if node.val == startValue:
                start_path.extend(path)
            
            if node.val == destValue:
                end_path.extend(path)

            if start_path and end_path:
                return
            
            path.append("L")
            helper(node.left)
            path.pop()

            if start_path and end_path:
                return

            path.append("R")
            helper(node.right)
            path.pop()

        helper(root)

        i = 0
        while i<len(start_path) and i<len(end_path) and start_path[i] == end_path[i]:
            i += 1

        return "U"*(len(start_path) - i) + "".join(end_path[i:])


        