class Solution:
    def clumsy(self, n: int) -> int:
        # ans = cur = n
        # opt_idx = 4

        # opt = {
        #     1 : lambda a,b : a-b, 
        #     2 : lambda a,b : a+b,
        #     3 : lambda a,b : int(a/b),
        #     4 : lambda a,b : a*b
        # }

        # while cur>=2:


        #     if opt == 0:
        #         opt = 4
            
        #     ans = opt[opt_idx](ans,cur-1)
        #     cur -= 1
        #     opt_idx -= 1
        
        # return ans

        stack =[n]
        cur = n-1
        opt_idx = 4

        opt = {
            3 : lambda a,b : int(a/b),
            4 : lambda a,b : a*b
        }

        while cur>=1:
            if opt_idx == 1:
                stack.append(-cur)
            
            elif opt_idx == 2:
                stack.append(cur)
            
            else:
                stack[-1] = opt[opt_idx](stack[-1],cur)

            opt_idx -= 1
            cur -= 1

            if opt_idx == 0:
                opt_idx = 4
        
        return sum(stack)
