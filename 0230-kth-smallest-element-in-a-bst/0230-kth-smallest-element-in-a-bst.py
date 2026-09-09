# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Required output: k th smallest element from all the values
        Brute force: - append all the values in an array, sort the array, return kth element from right
        Key state:
        Invariant:
        Dangerous case:

        Pseudocode:
        take a max_heap of size k
        iterate through all the nodes and append value in max_heap
        if size of max_heap >k then remove top node, until size of max_heap !=k
        once all the nodes are iterated return -max_heap[0] as ans

        Complexity: TC - O(n log n), SC - O(n)
        '''

        max_heap = []

        def helper(node):
            if not node:
                return
                
            heapq.heappush(max_heap, -node.val)

            while len(max_heap) > k:
                heapq.heappop(max_heap)
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return -max_heap[0]


