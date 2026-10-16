class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     # dp[i][j] means: - operations to converd word1[i:] to word2[j:]
    #     # Last row initialization: = it will be n-j operations
    #     # Last column initialization: it will be m-i operations
    #     # Row direction: right to left
    #     # Column direction: right to left
    #     # Final return cell: dp[0][0]

    #     m = len(word1)
    #     n = len(word2)

    #     def solve(i,j):
    #         if i>=m:
    #             return n-j
            
    #         if j>=n:
    #             return m-i
            
    #         if word1[i] == word2[j]:
    #             return solve(i+1,j+1)
            
    #         return 1 + min(solve(i+1,j), solve(i,j+1), solve(i+1,j+1))
        
    #     return solve(0,0)

    # def minDistance(self, word1: str, word2: str) -> int:
    #     # dp[i][j] means: - operations to converd word1[i:] to word2[j:]
    #     # Last row initialization: = it will be n-j operations
    #     # Last column initialization: it will be m-i operations
    #     # Row direction: right to left
    #     # Column direction: right to left
    #     # Final return cell: dp[0][0]

    #     m = len(word1)
    #     n = len(word2)
    #     dp = {}

    #     def solve(i,j):
    #         if i>=m:
    #             return n-j
            
    #         if j>=n:
    #             return m-i

    #         state = (i,j)
            
    #         if state in dp:
    #             return dp[state]

    #         if word1[i] == word2[j]:
    #             dp[state] = solve(i+1,j+1)
    #         else:
    #             dp[state] = 1 + min(solve(i+1,j), solve(i,j+1), solve(i+1,j+1))
            
    #         return dp[state]
        
    #     return solve(0,0)


    # def minDistance(self, word1: str, word2: str) -> int:
    #     # dp[i][j] means: - operations to converd word1[i:] to word2[j:]
    #     # Last row initialization: = it will be n-j operations
    #     # Last column initialization: it will be m-i operations
    #     # Row direction: right to left
    #     # Column direction: right to left
    #     # Final return cell: dp[0][0]

    #     m = len(word1)
    #     n = len(word2)
    #     dp = [[0]*(n+1) for _  in range(m+1)]

    #     for i in range(m):
    #         dp[i][n] = m-i
        
    #     for j in range(n):
    #         dp[m][j] = n-j

    #     for i in range(m-1,-1,-1):
    #         for j in range(n-1,-1,-1):
    #             if word1[i] == word2[j]:
    #                 dp[i][j] = dp[i+1][j+1]
    #             else:
    #                 dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        
    #     return dp[0][0]

    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] means: - operations to converd word1[i:] to word2[j:]
        # Last row initialization: = it will be n-j operations
        # Last column initialization: it will be m-i operations
        # Row direction: right to left
        # Column direction: right to left
        # Final return cell: dp[0][0]

        m = len(word1)
        n = len(word2)
        dp = [(n-j) for j in range(n+1)]

        for i in range(m-1,-1,-1):
            diagonal = dp[n]
            dp[n] = m-i
            for j in range(n-1,-1,-1):
                below = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = diagonal
                else:
                    dp[j] = 1 + min(dp[j], dp[j+1], diagonal)
                
                diagonal = below
        
        return dp[0]
