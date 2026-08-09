class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_heap = [(-f,key) for key, f in freq.items()]
        heapq.heapify(max_heap)
        
        ans = []

        while max_heap:
            f1, ch1 = heapq.heappop(max_heap)
            
            if ans and ch1 == ans[-1]:
                if not max_heap:
                    return ""
                f2, ch2 = heapq.heappop(max_heap)
                ans.append(ch2)

                if f2+1<0:
                    heapq.heappush(max_heap,(f2+1,ch2))
            
            else:
                ans.append(ch1)
                f1 += 1
            
            if f1 < 0:
                heapq.heappush(max_heap,(f1,ch1))
        
        return "".join(ans)
