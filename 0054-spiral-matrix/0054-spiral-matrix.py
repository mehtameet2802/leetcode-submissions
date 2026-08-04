class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        ans = []

        top = 0
        bottom = r-1
        left = 0
        right = c-1

        while left <= right and top<=bottom:
            
            j = left
            while j<=right:
                ans.append(matrix[top][j])
                j += 1
            
            top+=1
            i = top
            while i<=bottom:
                ans.append(matrix[i][right])
                i += 1
            
            right-=1
            j = right

            if top <= bottom:
                while j>=left:
                    ans.append(matrix[bottom][j])
                    j -= 1
            
                bottom -= 1
            i = bottom

            if left <= right:
                while i>=top:
                    ans.append(matrix[i][left])
                    i-=1

                left+=1
        
        return ans
        