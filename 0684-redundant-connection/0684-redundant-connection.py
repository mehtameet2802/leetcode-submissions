class DSU:

    def __init__(self,n):
        self.parent = [idx for idx in range(n+1)] 
        self.size = [1]*(n+1)
    
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, first, second):
        first_parent = self.find(first)
        second_parent = self.find(second)

        if first_parent == second_parent:
            return False

        if self.size[first_parent] < self.size[second_parent]:
            first_parent, second_parent = second_parent, first_parent
        
        self.parent[second_parent] = first_parent
        self.size[first_parent] += self.size[second_parent]

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        What makes an edge redundant?
        What information must be known before accepting an edge?
        How will connected components be represented?
        How are two components combined?
        What condition identifies the answer?
        Invariant:
        Complexity: SC - O(V), TC - O(E)

        I think we should DSU, as in this problem the edges are provided one after other and its asked to determine of adding this edge will lead to a cycle or not, a cycle occur if we cannot union as the parent of the nodes in new edge being added is already same, hence new edge cannot be added, and the very first edge that cannot be added by union is out answer
        '''

        dsu = DSU(len(edges))

        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
