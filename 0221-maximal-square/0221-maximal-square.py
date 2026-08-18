class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
        max_side = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = 1+min(
                        dp[r+1][c],
                        dp[r][c+1],
                        dp[r][c]
                    )
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side*max_side