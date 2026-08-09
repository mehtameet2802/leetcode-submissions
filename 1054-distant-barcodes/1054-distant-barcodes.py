class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        ans = []

        freq = Counter(barcodes)

        max_heap = [(-f,val) for val,f in freq.items()]
        heapq.heapify(max_heap)

        while max_heap:
            f1, ele1 = heapq.heappop(max_heap)

            if ans and ele1 == ans[-1]:
                f2, ele2 = heapq.heappop(max_heap)

                ans.append(ele2)

                if f2 + 1 < 0:
                    heapq.heappush(max_heap,(f2+1,ele2))
            else:
                ans.append(ele1)
                f1 += 1
            
            if f1 < 0:
                heapq.heappush(max_heap,(f1,ele1))
        
        return ans