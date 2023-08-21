class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i in range(len(nums)):
            x = target-nums[i]
            if x not in d1:
                d1[nums[i]] = i
            else:
                return [i,d1[x]]
        return [0,0]
