class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mem = {}

        n = len(prices)

        profit = float('-inf')

        def helper(i, have_stock, val):

            if (i,have_stock,val) in mem:
                return mem[i,have_stock,val]

            if i>=n:
                return 0
            
            if have_stock:
                a1 = helper(i+2, False, 0) + val+prices[i]
            else:
                a1 = helper(i+1, True, val-prices[i])
            
            a2 = helper(i+1, have_stock, val)
            ans = max(a1,a2)

            mem[(i,have_stock,val)] = ans
            return ans

        return helper(0, False, 0)
        return profit