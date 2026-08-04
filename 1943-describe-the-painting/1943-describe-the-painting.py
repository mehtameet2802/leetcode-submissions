from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        '''
        Pattern - Sweep Line + Difference Map

        TC - O(N log N)
        SC - O(N)
        '''

        events = defaultdict(int)

        for s,e,color in segments:
            events[s] += color
            events[e] -= color 
        
        points = sorted(events.keys())

        ans = []
        cur = 0
        for i in range(len(points)-1):
            cur += events[points[i]]

            if cur > 0:
                ans.append([points[i], points[i+1], cur])

        return ans