class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=0:
                while z<n and nums[z]!=0:
                    z+=1
                
                if i>z:
                    x = nums[i]
                    nums[i]=nums[z]
                    nums[z]=x
                    z+=1
        