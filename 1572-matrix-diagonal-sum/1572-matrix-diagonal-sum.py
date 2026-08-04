class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        r = len(mat)
        c = len(mat[0])

        i = j = 0
        while i < r:
            ans += mat[i][j]
            i += 1
            j += 1
        
        i = 0
        j = c-1
        while i < r:
            if i == j:
                i += 1
                j -= 1
                continue
            ans += mat[i][j]
            i += 1
            j -= 1
        
        return ans