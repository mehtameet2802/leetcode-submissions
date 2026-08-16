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
    def equationsPossible(self, equations: List[str]) -> bool:
        
        dsu = DSU(26)

        for eq in equations:
            if eq[1:3] == "==":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                dsu.union(a,b)

        for eq in equations:
            if eq[1:3] == "!=":
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')

                if dsu.find(a) == dsu.find(b):
                    return False
        
        return True