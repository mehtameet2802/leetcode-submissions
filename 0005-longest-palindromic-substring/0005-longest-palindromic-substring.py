class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(i,j):

            while i>=0 and j<len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return i+1,j-1 

        ans = ""
        for i in range(len(s)):
            l1,r1 = expand(i,i)
            l2,r2 = expand(i,i+1)

            if r1-l1+1 > r2-l2+1:
                cur = s[l1:r1+1]
            else:
                cur = s[l2:r2+1]

            if len(ans) < len(cur):
                ans = cur
            
        return ans