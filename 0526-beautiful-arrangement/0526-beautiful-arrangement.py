class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        path = []
        seen = set()

        def possible():
            for i, num in enumerate(path):
                if num % (i+1) != 0 and (i+1)%num != 0:
                    return False
            return True
        
        # def possibility()

        def helper():
            nonlocal ans

            if len(path) == n:
                if possible():
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