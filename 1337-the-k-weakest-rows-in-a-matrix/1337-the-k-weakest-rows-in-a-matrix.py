import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # max_heap = []
        
        # for i in range(len(mat)):
        #     cnt_1 = sum(mat[i])
        #     heapq.heappush(max_heap,(-cnt_1,-i))

        #     if len(max_heap) > k:
        #         heapq.heappop(max_heap)
        
        # ans = [0]*k
        # for j in range(k-1,-1,-1):
        #     ans[j] = (-heapq.heappop(max_heap)[1])
        
        # return ans


        max_heap = []
        
        for i in range(len(mat)):
            cnt_1 = bisect_left(mat[i],0,key = lambda x:-x)
            heapq.heappush(max_heap,(-cnt_1,-i))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = [0]*k
        for j in range(k-1,-1,-1):
            ans[j] = (-heapq.heappop(max_heap)[1])
        
        return ans