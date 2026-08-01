import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap = []
        f_map = Counter(s)

        for ch, f in f_map.items():
            heapq.heappush(max_heap, (-f,ch))
        
        ans = ""
        while max_heap:
            f, ch = heapq.heappop(max_heap)
            ans += (ch*-f)
            
        return ans