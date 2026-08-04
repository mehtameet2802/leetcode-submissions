class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        '''
        Pattern - Matrix Traversal

        TC - O(m*n)
        SC - O(r*c), O(1)
        '''

        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat
        
        ans = [[0]*c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                flatten_index = i * n + j

                nr = flatten_index // c
                nc = flatten_index % c

                ans[nr][nc] = mat[i][j]
        
        return ans

