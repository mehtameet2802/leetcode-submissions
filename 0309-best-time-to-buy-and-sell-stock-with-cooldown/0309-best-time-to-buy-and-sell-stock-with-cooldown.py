class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        Pattern - Recursion + DP

        TC - O(n)
        SC - O(n)
        '''

        mem = {}

        n = len(prices)

        profit = float('-inf')

        def helper(i, have_stock):

            if (i,have_stock) in mem:
                return mem[(i,have_stock)]

            if i>=n:
                return 0
            
            if have_stock:
                a1 = helper(i+2, False) + prices[i]
            else:
                a1 = helper(i+1, True) - prices[i]
            
            a2 = helper(i+1, have_stock)
            ans = max(a1,a2)

            mem[(i,have_stock)] = ans
            return ans

        return helper(0, False)


        '''
        Pattern - Recursion + DP

        TC - O(n)
        SC - O(1)
        '''

        mem = {}

        n = len(prices)

        profit = float('-inf')

        def helper(i, have_stock):

            if (i,have_stock) in mem:
                return mem[(i,have_stock)]

            if i>=n:
                return 0
            
            if have_stock:
                a1 = helper(i+2, False) + prices[i]
            else:
                a1 = helper(i+1, True) - prices[i]
            
            a2 = helper(i+1, have_stock)
            ans = max(a1,a2)

            mem[(i,have_stock)] = ans
            return ans

        return helper(0, False)