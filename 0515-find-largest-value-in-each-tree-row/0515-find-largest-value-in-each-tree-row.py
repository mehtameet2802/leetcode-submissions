# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Pattern:
        - Binary Tree
        - BFS
        - Queue
        - Level Order

        TC - O(N)
        SC - O(W)
        '''
        ans = []

        if not root:
            return ans

        queue = deque([])
        queue.append(root)

        while queue:

            length = len(queue)

            cur = -float('inf')
            for i in range(length):
                ele = queue.popleft()

                cur = max(cur,ele.val)

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            ans.append(cur)

        return ans