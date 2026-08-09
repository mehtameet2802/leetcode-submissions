class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        Pattern:
        - Min Heap
        - Set for duplicate prevention

        TC - O(n * p * log(n * p))
        SC - O(n * p)

        p = len(primes)
        '''

        min_heap = [1]
        seen = {1}

        while n>1:
            ele = heapq.heappop(min_heap)

            for num in primes:
                if num*ele in seen:
                    continue
                
                heapq.heappush(min_heap,ele*num)
                seen.add(ele*num)

            n -= 1
        
        return heapq.heappop(min_heap)