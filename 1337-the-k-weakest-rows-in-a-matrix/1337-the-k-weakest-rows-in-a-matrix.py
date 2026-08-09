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


        '''
        Pattern:
        - Binary Search → count 1s in each sorted row
        - Max Heap → keep only K weakest rows

        Why Max Heap?
        We want K weakest rows.
        So when heap size > K, remove the strongest row.

        Store:
        (-soldiers, -index)

        Negative values simulate a max heap using Python's min heap.

        TC:
        O(m log n + m log k)

        m = number of rows
        n = number of columns

        For every row:
        - bisect_left → O(log n)
        - heap push/pop → O(log k)

        SC:
        O(k)
        '''

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