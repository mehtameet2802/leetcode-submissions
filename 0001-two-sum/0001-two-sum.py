class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        c_map = {}

        for i, num in enumerate(nums):
            if target - num in c_map:
                ans = [c_map[target-num],i]
                return ans
            c_map[num] = i
        
        return []

        