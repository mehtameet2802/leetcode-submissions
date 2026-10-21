class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        n = len(intervals)
        end = intervals[0][1]
        remove = 0
        for i in range(1,n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                continue
            else:
                remove += 1

        return remove
