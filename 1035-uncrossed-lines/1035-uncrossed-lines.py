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

    # def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    #     n1 = len(nums1)
    #     n2 = len(nums2)

    #     dp = {}
    #     def solve(i,j):
    #         if i>=n1 or j>=n2:
    #             return 0
            
    #         state = (i,j)

    #         if state in dp:
    #             return dp[state]

    #         if nums1[i] == nums2[j]:
    #             dp[state] = 1 + solve(i+1,j+1)
    #         else:
    #             dp[state] = max(solve(i+1,j), solve(i,j+1))
            
    #         return dp[state]
        
    #     return solve(0,0)


    # def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    #     m = len(nums1)
    #     n = len(nums2)

    #     dp = [[0]*(n+1) for _ in range(m+1)]

    #     for i in range(m-1,-1,-1):
    #         for j in range(n-1,-1,-1):
    #             if nums1[i] == nums2[j]:
    #                 dp[i][j] = 1 + dp[i+1][j+1]
    #             else:
    #                 dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
    #     return dp[0][0]


    # def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    #     m = len(nums1)
    #     n = len(nums2)

    #     nxt = [0]*(n+1)

    #     for i in range(m-1,-1,-1):
    #         cur = [0]*(n+1)
    #         for j in range(n-1,-1,-1):
    #             if nums1[i] == nums2[j]:
    #                 cur[j] = 1 + nxt[j+1]
    #             else:
    #                 cur[j] = max(nxt[j], cur[j+1])
    #         nxt = cur

    #     return nxt[0]


    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [0]*(n+1)

        for i in range(m-1,-1,-1):
            diagonal = 0 
            for j in range(n-1,-1,-1):
                below = dp[j]
                if nums1[i] == nums2[j]:
                    dp[j] = 1 + diagonal
                else:
                    dp[j] = max(dp[j], dp[j+1])
                
                diagonal = below

        return dp[0]