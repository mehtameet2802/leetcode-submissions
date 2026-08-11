class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        min_heap = []

        times = [(arrival, departure, idx) for idx, (arrival, departure) in enumerate(times)]
        times.sort()

        available = list(range(n))
        heapq.heapify(available)

        for start, end, idx in times:
            
            while min_heap and min_heap[0][0] <= start:
                _, chair = heapq.heappop(min_heap)

                heapq.heappush(available,chair)
            
            chair = heapq.heappop(available)

            if idx == targetFriend:
                return chair
            
            heapq.heappush(min_heap,(end,chair))

        return -1
