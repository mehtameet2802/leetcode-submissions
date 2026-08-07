class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = []

        for ele in nums:
            points.append((ele[0],1))
            points.append((ele[1]+1,-1))
        
        cur = 0
        points.sort()
        prev = None
        ans = 0

        for point in points:
            
            if prev is not None and cur > 0:
                ans += point[0] - prev
                
            cur += point[1]
            prev = point[0]

        return ans