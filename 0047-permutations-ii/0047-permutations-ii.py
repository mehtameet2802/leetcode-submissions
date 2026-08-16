class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = set()

        def helper():
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):

                if i in used:
                    continue
                
                if i>0 and nums[i] == nums[i-1] and i-1 in used:
                    continue

                used.add(i)
                path.append(nums[i])
                helper()
                path.pop()
                used.remove(i)
        
        helper()
        return ans
