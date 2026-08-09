import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []

        for gift in gifts:
            heapq.heappush(max_heap,-gift)

        while k>0:
            cur = -heapq.heappop(max_heap)
            cur = int(pow(cur,0.5))
            heapq.heappush(max_heap,-cur)
            k -= 1
        
        return -sum(max_heap)