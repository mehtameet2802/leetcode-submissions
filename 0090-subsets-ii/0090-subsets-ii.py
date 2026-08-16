class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        nums.sort()
        
        def subsets(i):
            ans.append(path.copy())

            for j in range(i, len(nums)):
                if j>i and nums[j-1] == nums[j]:
                    continue
                path.append(nums[j])
                subsets(j+1)
                path.pop()
            
        subsets(0)
        return ans