# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Definition for a binary tree node.
        '''

        TC - O(N)
        SC - O(W)
        '''
        ans = -float('inf')

        if not root:
            return ans

        queue = deque([])
        queue.append(root)
        depth = 1
        level = -1

        while queue:

            length = len(queue)

            cur = 0
            for i in range(length):
                ele = queue.popleft()

                cur += ele.val

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            if cur > ans:
                level = depth
                ans = max(ans,cur)
            depth += 1

        return level