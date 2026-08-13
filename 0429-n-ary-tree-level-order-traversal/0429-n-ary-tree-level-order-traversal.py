"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        Pattern:
        - N-ary Tree
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
            cur = []

            for i in range(length):
                ele = queue.popleft()
                
                for child in ele.children:
                    queue.append(child)
                
                cur.append(ele.val)
            
            ans.append(cur)

        return ans