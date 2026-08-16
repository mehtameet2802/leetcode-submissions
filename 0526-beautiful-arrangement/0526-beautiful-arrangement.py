class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        seen = set()

        def helper(idx):
            nonlocal ans

            if idx == n+1:
                ans += 1
                return
            
            for i in range(1,n+1):
                if i in seen:
                    continue
                
                if i % idx == 0 or idx % i == 0:
                    seen.add(i)
                    helper(idx+1)
                    seen.remove(i)
        
        helper(1)
        return ans