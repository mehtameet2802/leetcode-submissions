class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        Pattern - Sort + Greedy

        TC - O(N log N)
        SC - O(1)
        '''

        nums.sort()

        total = 0

        for i, num in enumerate(nums):
            if i%2 == 0:
                total += num
        
        return total