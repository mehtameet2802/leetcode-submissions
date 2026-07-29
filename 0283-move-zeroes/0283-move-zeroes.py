class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0

        while r<len(nums):
            if nums[r]!=0:
                r+=1
                continue
            
            w = r+1

            while w<len(nums) and nums[w]==0:
                w+=1
            
            if w<len(nums):
                nums[r], nums[w] = nums[w], nums[r]
            else:
                break

            r+=1


            