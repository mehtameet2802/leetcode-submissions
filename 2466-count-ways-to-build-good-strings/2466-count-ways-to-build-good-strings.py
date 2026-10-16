class Solution:
    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
    #     def solve(length):
    #         if length > high:
    #             return 0

    #         way = 0
    #         if length >= low:
    #             way = 1
            
    #         way += solve(length + zero)
    #         way += solve(length + one)
            
    #         return way
        
    #     return solve(0)%(pow(10,9)+7)

    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
    #     dp = {}
    #     def solve(length):
    #         if length > high:
    #             return 0

    #         if length in dp:
    #             return dp[length]

    #         way = 0
    #         if length >= low:
    #             way = 1
            
    #         way += solve(length + zero)
    #         way += solve(length + one)
            
    #         dp[length] = way

    #         return dp[length]
        
    #     return solve(0)%(pow(10,9)+7)


    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = [0]*(high+zero+one)

        for length in range(high,-1,-1):
            if length >= low:
                dp[length] = 1

            dp[length] += dp[length+zero]
            dp[length] += dp[length+one]
        
        return dp[0]%(pow(10,9)+7)