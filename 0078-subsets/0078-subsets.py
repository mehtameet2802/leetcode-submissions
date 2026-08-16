class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def helper(i):
            ans.append(path.copy())
            
            for j in range(i,len(nums)):
                path.append(nums[j])
                helper(j+1)
                path.pop()
        
        helper(0)
        return ans
