# class Solution:
#     def lastStoneWeightII(self, stones: list[int]) -> int:
#         total = sum(stones)
#         target = total // 2
#         n = len(stones)

#         dp = [[False]*(target+1) for _ in range (n+1)]

#         for i in range(n):
#             dp[i][target] = True

#         for i in range(n-1,-1,-1):
#             for val in range(target-1,-1,-1):

#                 skip = dp[i+1][val] 

#                 take = False
#                 if val + stones[i] <= target:
#                     take = dp[i+1][val+stones[i]]
                
#                 dp[i][val] = skip or take
        
#         for j in range(target-1,-1,-1):
#             if dp[0][j] == True:
#                 return total - 2 *j
        
#         return 0

class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)

        dp = [[False]*(target+1) for _ in range (n+1)]

        dp[n][0] = True

        for i in range(n-1,-1,-1):
            for val in range(target+1):

                skip = dp[i+1][val] 

                take = False
                if val >= stones[i]:
                    take = dp[i+1][val-stones[i]]
                
                dp[i][val] = skip or take
        
        for j in range(target,-1,-1):
            if dp[0][j] == True:
                return total - 2 *j
        
        return 0