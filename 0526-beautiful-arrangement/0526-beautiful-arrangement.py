class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        path = []
        seen = set()

        def helper():
            nonlocal ans

            if len(path) == n:
                ans += 1
            
            for i in range(1,n+1):
                if i in seen:
                    continue
                
                idx = len(path) + 1
                if i % idx == 0 or idx % i == 0:
                    seen.add(i)
                    path.append(i)
                    helper()
                    path.pop()
                    seen.remove(i)
        
        helper()
        return ans