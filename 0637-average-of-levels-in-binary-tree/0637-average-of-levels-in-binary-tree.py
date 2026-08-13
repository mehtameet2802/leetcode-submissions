# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        Pattern:
        - Binary Tree
        - BFS
        - Level Order
        - Queue

        TC - O(N)
        Auxiliary SC - O(W)
        Worst-case SC - O(N)
        Output - O(H)
        '''

        queue = deque([])
        queue.append(root)
        ans = []

        while queue:
            length = len(queue)

            cur = 0

            for _ in range(length):
                ele = queue.popleft()
                cur += ele.val

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            avg = cur / length
            ans.append(avg)
        
        return ans