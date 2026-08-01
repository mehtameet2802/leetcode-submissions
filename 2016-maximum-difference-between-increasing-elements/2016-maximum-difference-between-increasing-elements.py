class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        '''
        Pattern - Prefix Minimum (Running Minimum)

        N = len(nums)

        Time Complexity: O(N)
        Space Complexity: O(1)
        '''

        min_ele = nums[0]
        ans = -1

        for i in range(1, len(nums)):
            if nums[i] > min_ele:
                ans = max(ans, nums[i] - min_ele)
            else:
                min_ele = nums[i]

        return ans