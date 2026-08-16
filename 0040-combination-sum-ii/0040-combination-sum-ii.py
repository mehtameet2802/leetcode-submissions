class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def helper(i, cur):
            if cur == target:
                ans.append(path.copy())
                return

            if cur>target:
                return
            
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                
                path.append(candidates[j])
                helper(j+1, cur+candidates[j])
                path.pop()
            
        helper(0,0)
        return ans