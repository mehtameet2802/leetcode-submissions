class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # '''
        # Pattern - Sort + Scan

        # TC - O(N log N)
        # SC - O(1)
        # '''

        # citations.sort()

        # n = len(citations)
        # l = 0
        # r = n - 1

        # while l<=r:
        #     papers = r - l + 1

        #     if citations[l] >= papers:
        #         return r - l +1
        #     else:
        #         l += 1
        
        # return 0


        '''
        Pattern - Bucket Sort

        TC - O(N)
        SC - O(N)
        '''

        n = len(citations)
        buckets = n+1
        count_arr = [0]*buckets

        for c in citations:
            if c >= n:
                count_arr[n] += 1
            else:
                count_arr[c] += 1

        papers = 0
        for h in range(n,-1,-1):
            papers += count_arr[h] 

            if papers >= h:
                return h
        