class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
        squares = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 1:
                    dp[r+1][c+1] = 1+min(
                        dp[r+1][c],
                        dp[r][c+1],
                        dp[r][c]
                    )
                    squares += dp[r+1][c+1]

        return squares