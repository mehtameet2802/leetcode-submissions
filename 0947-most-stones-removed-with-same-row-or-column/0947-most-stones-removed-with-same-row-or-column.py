class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        return True


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        dsu = DSU(len(stones))

        cnt = 0
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                x1, y1 = stones[i]
                x2, y2 = stones[j]

                # if dsu_x.union(x1,x2) or dsu_y.union(y1,y2):
                #     cnt += 1

                if x1 == x2 or y1 == y2:
                    if dsu.union(i,j):
                        cnt += 1
        
        return cnt