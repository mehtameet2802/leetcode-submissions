# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Pattern:
        - Binary Tree
        - BFS
        - Queue
        - Level Order

        TC - O(N)
        SC - O(W)
        Worst case SC - O(N)
        '''
        ans = []

        if not root:
            return ans

        queue = deque([])
        queue.append(root)

        while queue:

            length = len(queue)
            cur = []

            for _ in range(length):
                ele = queue.popleft()
                cur.append(ele.val)

                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
            
            ans.append(cur.copy())

        return ans