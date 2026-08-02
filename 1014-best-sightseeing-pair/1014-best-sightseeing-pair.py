class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        '''
        Pattern - Greedy + Prefix Maximum

        TC - O(N)
        SC - O(1)
        '''
        
        best = values[0] + 0
        ans = -float('inf')

        for j in range(1,len(values)):
            ans = max(ans, best + values[j] - j)
            best = max(best, values[j] + j)
        
        return ans