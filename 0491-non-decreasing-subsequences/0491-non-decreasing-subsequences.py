class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()

        ans = []
        path = []

        def helper(i):
            if len(path) >= 2:
                ans.append(path.copy())

            used = set()
            
            for j in range(i, len(nums)):
                
                if nums[j] in used:
                    continue

                if path and path[-1] > nums[j]:
                    continue

                used.add(nums[j])
                
                path.append(nums[j])
                helper(j+1)
                path.pop()

        helper(0)
        return ans