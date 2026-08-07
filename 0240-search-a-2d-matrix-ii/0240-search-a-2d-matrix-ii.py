class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Pattern - Staircase Search/Matrix Elimination

        TC - O(r+c)
        SC - O(1)
        '''

        ROWS = len(matrix)
        COLS = len(matrix[0])

        r = 0
        c = COLS -1

        while r < ROWS and c >= 0:

            if matrix[r][c] == target:
                return True

            elif matrix[r][c] > target:
                c -= 1

            else:
                r += 1 
        
        return False