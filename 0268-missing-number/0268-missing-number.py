class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        '''
        Pattern - XOR

        TC - O(N)
        SC - O(1)
        '''
        
        ans = len(nums)

        for i, num in enumerate(nums):
            ans = ans^i^num
        
        return ans