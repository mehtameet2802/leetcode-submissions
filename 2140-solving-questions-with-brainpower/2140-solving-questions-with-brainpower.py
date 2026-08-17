class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = {}

        def helper(i):
            if i in dp:
                return dp[i]

            if i>=len(questions):
                return 0
            
            take =  questions[i][0] + helper(questions[i][1] + 1 + i)
            skip = helper(1 + i)

            
            dp[i] = max(take, skip)
            return dp[i]
        
        return helper(0)