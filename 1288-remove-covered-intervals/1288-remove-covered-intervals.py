class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        cnt = 0
        maxEnd = 0

        for start, end in intervals:
            if end > maxEnd:
                maxEnd = end
                cnt += 1
        
        return cnt