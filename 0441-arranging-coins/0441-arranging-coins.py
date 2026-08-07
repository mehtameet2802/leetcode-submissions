class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        Pattern - Binary Search on Answer
        TC - TC - O(n * log(sum(weights)))
        SC - O(1)
        '''

        coins = n

        l = 1
        r = n

        def calc(rows):
            return rows * (rows+1)//2

        while l < r:
            mid = l + (r- l + 1)//2

            if calc(mid) <= coins:
                l = mid
            else:
                r = mid - 1
        
        return l