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


        # ans = 0
        # path = []
        # seen = set()

        # def helper():
        #     nonlocal ans

        #     if len(path) == n:
        #         ans += 1
        #         return
            
        #     for i in range(1,n+1):
        #         if i in seen:
        #             continue
                
        #         idx = len(path) + 1
        #         if i % idx == 0 or idx % i == 0:
        #             seen.add(i)
        #             path.append(i)
        #             helper()
        #             path.pop()
        #             seen.remove(i)
        
        # helper()
        # return ans