class Solution:
    # def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    #     n1 = len(nums1)
    #     n2 = len(nums2)

    #     def solve(i,j):
    #         if i>=n1 or j>=n2:
    #             return 0
            
    #         if nums1[i] == nums2[j]:
    #             return 1 + solve(i+1,j+1)
            
    #         return max(solve(i+1,j), solve(i,j+1))
        
    #     return solve(0,0)

    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = {}
        def solve(i,j):
            if i>=n1 or j>=n2:
                return 0
            
            state = (i,j)

            if state in dp:
                return dp[state]

            if nums1[i] == nums2[j]:
                dp[state] = 1 + solve(i+1,j+1)
            else:
                dp[state] = max(solve(i+1,j), solve(i,j+1))
            
            return dp[state]
        
        return solve(0,0)