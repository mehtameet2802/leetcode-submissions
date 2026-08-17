class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}

        def helper(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            if r >= len(triangle) or c >= len(triangle[r]):
                return float('inf')

            if r == len(triangle)-1:
                return triangle[r][c]
            
            down_one = helper(r+1,c)
            down_two = helper(r+1,c+1)

            ans = min(down_one, down_two) + triangle[r][c]
            dp[(r,c)] = ans
            return ans
        
        return helper(0,0)