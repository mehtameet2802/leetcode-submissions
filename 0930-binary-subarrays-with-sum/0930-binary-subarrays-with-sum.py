class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # left = 0
        # window_sum = 0
        # total = sum(nums)

        # cnt = 0
        
        # for right, num in enumerate(nums):
        #     window_sum += num

        #     while window_sum > goal and left<=right:
        #         window_sum -= nums[left]
        #         left += 1
            
        #     if window_sum == goal:
        #         cnt += 1
        
        # return cnt

        prefix_sum = 0
        sums = defaultdict(int)
        cnt = 0
        sums[0] = 1

        for num in nums:
            prefix_sum += num

            required = prefix_sum - goal

            if required in sums:
                cnt += sums[required]
            
            sums[prefix_sum] += 1
        
        return cnt
            