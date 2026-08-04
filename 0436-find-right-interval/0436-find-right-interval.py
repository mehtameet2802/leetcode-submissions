from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        '''
        Patter - Sortign + Binary Search

        TC - O(N log N)
        SC - O(N)
        '''

        start_map = {}

        for i, (start,end) in enumerate(intervals):
            start_map[start] = i
        
        starts = sorted(start_map)

        ans = []
        for start, end in intervals:
            idx = bisect_left(starts, end)

            if idx >= len(starts):
                ans.append(-1)
            else:
                ans.append(start_map[starts[idx]])

        return ans