class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        TC = O(V + E)
        SC = O(V)
        '''

        in_degree = [0]*n

        for u,v in edges:
            in_degree[v] += 1
        
        ans = []
        for i in range(n):
            if in_degree[i] == 0:
                ans.append(i)
        
        return ans