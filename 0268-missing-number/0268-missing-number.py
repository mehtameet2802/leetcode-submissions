class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # '''
        # Pattern - SUM Property

        # TC - O(N)
        # SC - O(1)
        # '''

        # ans = sum(nums)
        # n = len(nums)

        # total = n*(n+1)//2
        # ans = total-ans
        
        # return ans

        '''
        Pattern - XOR

        TC - O(N)
        SC - O(1)
        '''
        
        ans = len(nums)

        for i, num in enumerate(nums):
            ans = ans^i^num
        
        return ans