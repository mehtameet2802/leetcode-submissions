class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ans = 0

        events = []

        for start, end in intervals:
            events.append((start,1))
            events.append((end+1,-1))

        events.sort()

        cur = 0
        for event in events:
            cur += event[1]
            ans = max(ans,cur)
        return ans