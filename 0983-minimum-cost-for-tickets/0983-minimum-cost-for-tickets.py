class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        last_day = days[-1]
        days = set(days)

        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in days:
                dp[day] = dp[day-1]
            else:
                dp[day] = min(
                    dp[max(0,day-1)] + costs[0],
                    dp[max(0,day-7)] + costs[1],
                    dp[max(0,day-30)] + costs[2]
                )
        
        return dp[last_day]