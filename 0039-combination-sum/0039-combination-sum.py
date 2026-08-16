class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []


        def helper(i, cur):
            if cur == target:
                ans.append(path.copy())
                return
            
            if cur > target:
                return
            
            for i in range(i,len(candidates)):
                path.append(candidates[i])
                helper(i, cur+candidates[i])
                path.pop()

        helper(0,0)
        return ans