class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        i = n-2

        while i>=0 and nums[i+1] <= nums[i]:
            i -= 1

        if i<0:
            nums = nums.reverse()
            return
        
        for j in range(n-1,i,-1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        
        nums[i+1:] = reversed(nums[i+1:])

                