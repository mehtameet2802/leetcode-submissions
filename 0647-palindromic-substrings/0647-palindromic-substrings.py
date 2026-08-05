class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Pattern - Exoand Around the Center

        TC - O(N^2)
        SC - O(1)
        '''

        def expand(i,j):
            
            cnt = 0

            while i>=0 and j<len(s) and s[i] == s[j]:
                i -= 1
                j += 1

                cnt += 1
            
            return cnt



        ans = 0
        for i in range(len(s)):
            ans += expand(i,i)
            ans += expand(i,i+1)
        
        return ans