class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda x: x[1] )
        arrows = 1
        n = len(points)

        end = points[0][1]

        for i in range(1,n):
            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
                        
        return arrows