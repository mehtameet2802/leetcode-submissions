class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Pattern - Binary Search
        TC - O(log n)
        SC - O(1)
        '''

        if x<2:
            return x

        l = 0
        r = x//2

        while l<=r:
            mid = l + (r-l)//2

            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return r