class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals)<2:
            return intervals
        
        intervals = sorted(intervals)
        ans = []
        a = intervals[0]

        for ele in intervals:
            if ele[0]<=a[1]:
                a[1] = max(ele[1],a[1])
                continue
            else:
                ans.append(a)
                a = ele
        
        ans.append(a)
        return ans