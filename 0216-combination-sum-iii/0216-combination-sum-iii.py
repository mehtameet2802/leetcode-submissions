class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def helper(i, cur):
            if len(path) == k and cur == n:
                ans.append(path.copy())
                return
            
            if len(path) > k  or cur > n:
                return
            
            for j in range(i,10):
                if cur + j > n:
                    break
                path.append(j)
                helper(j+1, cur + j)
                path.pop()
            
        helper(1,0)
        return ans