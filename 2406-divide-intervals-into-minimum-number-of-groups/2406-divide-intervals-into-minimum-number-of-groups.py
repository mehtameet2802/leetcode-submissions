class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        '''
        Pattern - Sweep Line

        TC - O(N log N)
            - Create 2N events: O(N)
            - Sort events: O(N log N)
            - Sweep events: O(N)

        SC - O(N)
            - Stores 2N events
        '''

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