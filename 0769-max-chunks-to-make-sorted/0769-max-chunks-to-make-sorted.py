class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        '''
        Pattern - Greedy (Prefix Maximum)

        TC - O(N)
        SC - O(1)
        '''

        cnt = 0
        mx = 0

        for i, num in enumerate(arr):
            mx = max(mx,num)

            if mx == i:
                cnt += 1
        
        return cnt