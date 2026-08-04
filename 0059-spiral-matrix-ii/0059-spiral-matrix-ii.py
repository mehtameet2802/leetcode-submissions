class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cur = 1

        left = 0
        right = n
        top = 0
        bottom = n

        matrix = [[0]*n for _ in range(n)]

        while left < right and top < bottom:
            
            j = left
            while j < right:
                matrix[top][j] = cur
                cur += 1
                j += 1
            top += 1
            i = top

            while i < bottom:
                matrix[i][right-1] = cur
                cur += 1
                i += 1
            
            right -= 1
            j = right-1

            if left<right:
                while j >= left:
                    matrix[bottom-1][j] = cur
                    cur += 1
                    j -= 1
                
                bottom -= 1
            
            i = bottom -1

            if top < bottom:
                while i >= top:
                    matrix[i][left] = cur
                    cur += 1
                    i -= 1
            
                left += 1
            

        return matrix

