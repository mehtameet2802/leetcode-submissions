import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # '''
        # TC - O(N log N)
        # SC - O(N)
        # '''

        # max_heap = []

        # for gift in gifts:
        #     heapq.heappush(max_heap,-gift)

        # while k>0:
        #     cur = -heapq.heappop(max_heap)
        #     cur = int(pow(cur,0.5))
        #     heapq.heappush(max_heap,-cur)
        #     k -= 1
        
        # return -sum(max_heap)


        '''
        Pattern:
        - Max Heap
        - Repeatedly extract the maximum

        TC - O(N + K log N)
        SC - O(N)

        heapify() → O(N)
        Each operation:
            pop maximum → O(log N)
            push new value → O(log N)
        K operations → O(K log N)
        '''
        max_heap = []

        for gift in gifts:
            max_heap.append(-gift)

        heapq.heapify(max_heap)    

        while k > 0:
            cur = -heapq.heappop(max_heap)

            # Leave floor(sqrt(cur)) gifts
            cur = isqrt(cur)

            heapq.heappush(max_heap, -cur)

            k -= 1

        return -sum(max_heap)