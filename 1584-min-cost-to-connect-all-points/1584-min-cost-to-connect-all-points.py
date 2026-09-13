class DSU:
    def __init__(self,n):
        self.parent = [idx for idx in range(n)]
        self.size = [1]*n

    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self,first,second):
        first_parent = self.find(first)
        second_parent = self.find(second)

        if first_parent == second_parent:
            return False
        
        if self.size[first] < self.size[second]:
            first_parent, second_parent = second_parent, first_parent
        
        self.parent[second_parent] = first_parent
        self.size[first_parent] += self.size[second_parent]

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        for i in range(len(points)):
            first_x, first_y = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                second_x, second_y = points[j][0], points[j][1]

                dist = abs(first_x-second_x) + abs(first_y-second_y)

                edges.append([dist,i,j])

        edges.sort()

        n = len(points)
        dsu = DSU(n)
        total_cost = 0
        edges_merged = 0

        for d,u,v in edges:
            if dsu.union(u,v):
                total_cost += d
                edges_merged += 1
            
            if edges_merged == n-1:
                break
        
        return total_cost

