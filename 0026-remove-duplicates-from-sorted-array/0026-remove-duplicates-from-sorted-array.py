class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        i = 0

        while i<len(nums):
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            
            nums[idx] = nums[i]
            idx+=1
            i+=1

        return idx