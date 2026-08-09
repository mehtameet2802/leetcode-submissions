class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        arr = [2,3,5]
        seen = set()

        while min_heap and n>1:
            ele = heapq.heappop(min_heap)

            for num in arr:
                if ele*num in seen:
                    continue
                heapq.heappush(min_heap,ele*num)
                seen.add(ele*num)
            
            n -= 1
        
        return heapq.heappop(min_heap)