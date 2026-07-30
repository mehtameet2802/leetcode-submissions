class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = -1
        n = len(nums)

        for num in nums:
            if cnt == 0:
                ele = num
                cnt = 1
            elif ele == num:
                cnt+=1
            else:
                cnt -= 1
        
        return ele