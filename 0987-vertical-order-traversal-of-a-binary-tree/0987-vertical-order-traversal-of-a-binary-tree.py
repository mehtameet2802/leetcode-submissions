# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_heap = []
        min_idx = float('inf')
        max_idx = -min_idx

        def helper(node,col,depth):
            nonlocal min_idx, max_idx

            if not node:
                return
            
            heapq.heappush(min_heap,(col,depth,node.val))
            min_idx = min(min_idx,col)
            max_idx = max(max_idx,col)
            
            helper(node.left,col-1,depth+1)
            helper(node.right,col+1,depth+1)
                
        
        helper(root,0,0)

        ans_length = max_idx - min_idx + 1
        ans = [[] for _ in range(ans_length)]

        while min_heap:
            col, depth, val = heapq.heappop(min_heap)
            ans[col - min_idx].append(val)

        return ans

