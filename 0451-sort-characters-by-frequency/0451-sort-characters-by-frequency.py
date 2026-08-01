import heapq
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        # '''
        # Pattern - Heaps

        # N - len of string 
        # TC - O(N log N)
        # SC - O(N)
        # '''

        # max_heap = []
        # f_map = Counter(s)

        # for ch, f in f_map.items():
        #     heapq.heappush(max_heap, (-f,ch))
        
        # ans = ""
        # while max_heap:
        #     f, ch = heapq.heappop(max_heap)
        #     ans += (ch*-f)
            
        # return ans


        '''
        Pattern - Heaps

        N - len of string 
        TC - O(N log N)
        SC - O(N)
        '''

        f_map = Counter(s)
        ans = []

        for ch, f in sorted(f_map.items(), key = lambda x:x[1], reverse=True):
            ans.append(ch*f)
            
        return "".join(ans)