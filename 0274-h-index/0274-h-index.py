class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)
        l = 0
        r = n - 1

        ans = 0 

        while l<=r:
            papers = r - l + 1

            if citations[l] >= papers:
                return r - l +1
            else:
                l += 1
        
        return 0