from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        ind = [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            ind[u] += 1
        
        queue = deque([])

        for i, ele in enumerate(ind):
            if ele == 0:
                queue.append(i)

        cnt = 0

        while queue:

            ele = queue.popleft()
            cnt+=1
            for nei in graph[ele]:
                ind[nei] -= 1

                if ind[nei] == 0:
                    queue.append(nei)
        
        return cnt == numCourses

