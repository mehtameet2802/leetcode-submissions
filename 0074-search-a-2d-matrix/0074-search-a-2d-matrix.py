class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Pattern - Binary Search
        TC - O(log n)
        SC - O(1)
        '''

        ROWS = len(matrix)
        COLS = len(matrix[0])
        s = 0
        e = ROWS*COLS-1

        while s<=e:

            mid = s + (e-s)//2
            r = mid // COLS
            c = mid % COLS

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                s = mid + 1
            else:
                e = mid - 1
        
        return False