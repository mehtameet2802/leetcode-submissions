class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        TC = O(N × 2^N)
        SC = O(N)
        '''
        path = []
        ans = []


        def helper(i):
            if len(path) == len(s):
                ans.append("".join(path))
                return
            
            for j in range(i,len(s)):
                if s[j].isalpha():
                    path.append(s[j].lower())
                    helper(j+1)
                    path.pop()

                    path.append(s[j].upper())
                    helper(j+1)
                    path.pop()
                else:
                    path.append(s[j])
                    helper(j+1)
                    path.pop()
            
        helper(0)
        return ans