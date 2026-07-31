import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # '''
        # Pattern - Heap + queue

        # k is number of unique task

        # TC - O(T log k) t is time, heap operation cost log k
        # SC - O(k)
        # '''


        # t_map = Counter(tasks)

        # max_heap = []

        # for t,c in t_map.items():
        #     heapq.heappush(max_heap,-c)
        
        # queue = deque([])

        # time = 0
        # while max_heap or queue:

        #     time+=1

        #     if max_heap:
        #         c = heapq.heappop(max_heap)
        #         c+=1

        #         if c!=0:
        #             queue.append((c,time+n))
            
        #     if queue and queue[0][1] == time:
        #         ele = queue.popleft()
        #         heapq.heappush(max_heap,ele[0])
        
        # return time

        '''
        Pattern - Greedy

        m - len(tasks)
        k - number of unqiue tasks

        TC - O(m)
        SC - O(k)
        '''

        f_map = Counter(tasks)

        max_f = max(f_map.values())

        max_f_ele = 0

        for t,f in f_map.items():
            if f == max_f:
                max_f_ele += 1
        
        total_time = max(len(tasks),(max_f-1)*(n+1)+max_f_ele)
        return total_time




