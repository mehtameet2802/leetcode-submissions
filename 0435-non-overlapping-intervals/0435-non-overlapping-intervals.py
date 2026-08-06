class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        removals = 0
        end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= end:
                end = interval[1]
            else:
                removals += 1
            
        return removals
