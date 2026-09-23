class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self,x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x,y):
        first = self.find(x)
        second = self.find(y)

        if first == second:
            return False
        
        if self.size[second] > self.size[first]:
            first, second = second, first
        
        self.parent[second] = first
        self.size[first] += self.size[second]

        return True

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        
        if len(connections) < n-1:
            return -1

        dsu = DSU(n)

        components = n

        for u,v in connections:
            if dsu.union(u,v):
                components -= 1
        
        return components - 1