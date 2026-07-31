class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        '''
        Pattern - Linear Search

        TC - O(n)
        SC - O(1)
        '''

        cnt = 0
        ans = 0
        for num in nums:
            if num == 0:
                ans = max(ans,cnt)
                cnt = 0
                continue
            
            cnt+=1

        return max(ans,cnt)