class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        '''
        Pattern - Sum + Greedy

        TC - O(N log N)
        SC - O(1)
        '''

        # points.sort()
        # arrows = 1

        # end = points[0][1]

        # for s,e in points[1:]:

        #     if s > end:
        #         arrows += 1
        #         end = e
        #     else:
        #         end = min(end,e)

        # return arrows 

        points.sort(key = lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for i in range(1,len(points)):

            if points[i][0] > end:
                arrows += 1
                end = points[i][1]
        
        return arrows

