class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        used = set()

        def helper():
            if len(path)== len(nums):
                ans.append(path.copy())

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                
                used.add(nums[i])
                path.append(nums[i])
                helper()
                path.pop()
                used.remove(nums[i])
        
        helper()
        return ans