class Solution:
    # def longestPalindromeSubseq(self, s: str) -> int:

    #     # dp[left][right] means: - longest palindromic sub string in s[l:r+1]
    #     # Smallest interval initialized: l == r, length 1
    #     # Which shorter intervals does a state read? - if s[l] == s[r],it checks s[l+1:r] else it checks s[l+1:r], s[l:r]
    #     # Should interval length grow or shrink? it should shrink
    #     # Valid fill order: - left - left to right, and right is bottom to up 
    #     # Final return cell: 


    #     n = len(s)
    #     def solve(l,r):
    #         if l>r:
    #             return 0
            
    #         if l == r:
    #             return 1
            
    #         if s[l] == s[r]:
    #             return 2 + solve(l+1,r-1)
    #         else:
    #             return max(solve(l+1,r), solve(l,r-1))
        
    #     return solve(0,n-1)


    def longestPalindromeSubseq(self, s: str) -> int:

        # dp[left][right] means: - longest palindromic sub string in s[l:r+1]
        # Smallest interval initialized: l == r, length 1
        # Which shorter intervals does a state read? - if s[l] == s[r],it checks s[l+1:r] else it checks s[l+1:r], s[l:r]
        # Should interval length grow or shrink? it should shrink
        # Valid fill order: - left - left to right, and right is bottom to up 
        # Final return cell: 


        n = len(s)
        dp = {}
        def solve(l,r):
            if l>r:
                return 0
            
            if l == r:
                return 1

            state = (l,r)

            if state in dp:
                return dp[state]
            
            if s[l] == s[r]:
                dp[state] =2 + solve(l+1,r-1)
            else:
                dp[state] = max(solve(l+1,r), solve(l,r-1))

            return dp[state]

        return solve(0,n-1)