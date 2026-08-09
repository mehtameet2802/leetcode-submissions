class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)

        max_heap = [(-f,key) for key,f in freq.items()]
        heapq.heapify(max_heap)

        ans = []
        while max_heap and k>0:
            f, word = heapq.heappop(max_heap)
            k -= 1
            ans.append(word)
        return ans
