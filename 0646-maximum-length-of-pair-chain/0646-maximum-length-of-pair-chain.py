class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        Pattern - Sort + Greedy
        TC - O(N log N)
        SC - O(1)
        '''
        pairs.sort(key = lambda x: x[1])

        ans = 1
        end = pairs[0][1]

        for pair in pairs:
            if pair[0] > end:
                end = pair[1]
                ans += 1
        
        return ans
