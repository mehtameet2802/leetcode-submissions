import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # '''
        # Pattern - Frequency Count

        # N - len(nums)
        # TC - O(N + M log M)
        # SC - O(N)
        # '''

        # f_map = Counter(nums)

        # ans = []

        # for val, f in sorted(f_map.items(),key=lambda x:x[1], reverse=True):
        #     if k>0:
        #         ans.append(val)
        #         k-=1
        #     else:
        #         break
        
        # return ans


        '''
        Pattern - Frequency Count

        N - len(nums)
        M - unique elements
        TC - O(N + M log k)
        SC - O(N)
        '''

        f_map = Counter(nums)
        min_heap = []
        ans = []

        for val, f in f_map.items():
            if min_heap and k==0: 
                if f > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (f,val))
            else:
                heapq.heappush(min_heap, (f,val))
                k-=1

        for item in min_heap:
            ans.append(item[1])

        return ans
