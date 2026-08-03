import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0]*1001
        for ele in trips:
            s = ele[1]
            e = ele[2]
            p = ele[0]

            arr[s] += p
            arr[e] -= p

        cur = 0
        for i in range(1001):
            cur += arr[i]

            if cur > capacity:
                return False
        
        return True

