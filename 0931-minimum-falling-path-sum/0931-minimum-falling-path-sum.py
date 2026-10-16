class Solution:
    # def minFallingPathSum(self, matrix: list[list[int]]) -> int:
    #     # Required output:
    #     # Valid starting positions: all the columns of row 0
    #     # Valid moves from one cell: go left diagonal, right diagonal, down by 1
    #     # What does solve(row, col) return? - cur cell val +  min of all the 2 moves
    #     # Base case: j>=n  or j<0: return inf, i>=n return 0
    #     # Invalid-column handling:
    #     # Recurrence:
    #     # How are multiple starting columns combined?
    #     # Expected memoized TC and SC:

    #     n = len(matrix)
    #     def solve(i,j):
    #         if j>=n or j<0:
    #             return float('inf')

    #         if i>=n:
    #             return 0
            
    #         return matrix[i][j] + min(solve(i+1,j),solve(i+1,j+1),solve(i+1,j-1))


    #     ans = float('inf')
    #     for i in range(n):
    #         ans = min(ans, solve(0,i))

    #     return ans

    # def minFallingPathSum(self, matrix: list[list[int]]) -> int:
    #     # Required output:
    #     # Valid starting positions: all the columns of row 0
    #     # Valid moves from one cell: go left diagonal, right diagonal, down by 1
    #     # What does solve(row, col) return? - cur cell val +  min of all the 2 moves
    #     # Base case: j>=n  or j<0: return inf, i>=n return 0
    #     # Invalid-column handling:
    #     # Recurrence:
    #     # How are multiple starting columns combined?
    #     # Expected memoized TC and SC:

    #     n = len(matrix)
    #     dp = {}
    #     def solve(i,j):
    #         if j>=n or j<0:
    #             return float('inf')

    #         if i>=n:
    #             return 0

    #         state = (i,j)

    #         if state in dp:
    #             return dp[state]

    #         dp[state] = matrix[i][j] + min(solve(i+1,j),solve(i+1,j+1),solve(i+1,j-1))
    #         return dp[state]


    #     ans = float('inf')
    #     for i in range(n):
    #         ans = min(ans, solve(0,i))

    #     return ans


    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        # Required output:
        # Valid starting positions: all the columns of row 0
        # Valid moves from one cell: go left diagonal, right diagonal, down by 1
        # What does solve(row, col) return? - cur cell val +  min of all the 2 moves
        # Base case: j>=n  or j<0: return inf, i>=n return 0
        # Invalid-column handling:
        # Recurrence:
        # How are multiple starting columns combined?
        # Expected memoized TC and SC:

        n = len(matrix)
        dp = [[0]*(n) for _ in range(n)]

        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(n):
                
                down_left = float('inf')
                if j > 0 :
                    down_left = dp[i+1][j-1]
                
                down_right = float('inf')
                if j<n-1:
                    down_right = dp[i+1][j+1]
                
                down = dp[i+1][j]

                dp[i][j] = matrix[i][j] + min(down, down_left, down_right)
        
        return min(dp[0])
