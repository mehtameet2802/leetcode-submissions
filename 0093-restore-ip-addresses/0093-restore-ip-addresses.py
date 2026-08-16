class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        K - number of ip address
        N - length of ip address
        ┌─────────────────────┐
        │ TC                  │
        │ O(3^4 × N) = O(N)   │
        ├─────────────────────┤
        │ Auxiliary SC        │
        │ O(1)                │
        ├─────────────────────┤
        │ Output SC           │
        │ O(K × N)            │
        └─────────────────────┘
        '''

        ans = []
        path = []

        def helper(i):

            if len(path) == 4:
                if  i >= len(s):
                    ans.append(".".join(path))
                    return
            
            for j in range(i, min(i+3,len(s))):
                part = s[i:j+1]

                if len(part)>1 and part[0]=='0':
                    break
                
                if int(part) > 255:
                    break

                path.append(part)
                helper(j+1)
                path.pop()
        
        helper(0)
        return ans