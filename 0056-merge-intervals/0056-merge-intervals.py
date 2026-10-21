class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:(x[0],x[1]))

        ans = []
        n = len(intervals)

        cur = intervals[0]
        for i in range(1,n):
            if intervals[i][0] <= cur[1]:
                cur[1] = max(intervals[i][1], cur[1])
            else:
                ans.append(cur)
                cur = intervals[i]
        
        ans.append(cur)
        return ans