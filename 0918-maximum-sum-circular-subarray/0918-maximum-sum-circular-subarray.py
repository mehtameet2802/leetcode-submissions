class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        '''
        Pattern - Kadane

        TC - O(N)
        SC - O(1)
        '''

        total = sum(nums)

        cur_max = best_max = nums[0]
        cur_min = best_min = nums[0]

        for num in nums[1:]:
            cur_max = max(num, num+cur_max)
            cur_min = min(num, num+cur_min)

            best_max = max(best_max, cur_max)
            best_min = min(best_min, cur_min)
        
        if best_max<0:
            return best_max
        
        return max(best_max, total-best_min)
