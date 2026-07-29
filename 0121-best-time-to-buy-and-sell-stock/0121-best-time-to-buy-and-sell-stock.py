class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = -float('inf')
        cur_min = float('inf')

        for num in prices:
            cur_min = min(cur_min,num)
            profit = num - cur_min
            ans = max(ans,profit)
        
        return ans