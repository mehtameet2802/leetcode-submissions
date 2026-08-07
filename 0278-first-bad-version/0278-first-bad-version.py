# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n+1

        while l < r:

            mid = l + (r-l)//2

            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        
        return l