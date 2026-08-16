class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def helper(i):
            if len(path) == k:
                ans.append(path.copy())
                return
            
            for j in range(i,n+1):
                path.append(j)
                helper(j+1)
                path.pop()
            
        helper(1)
        return ans
