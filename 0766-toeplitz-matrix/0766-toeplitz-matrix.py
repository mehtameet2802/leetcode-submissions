class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        # '''
        # Pattern - Matrix Traversal

        # TC - O(r*c)
        # SC - O(1)
        # '''

        # r = len(matrix)
        # c = len(matrix[0])

        # cur_r = 0
        # for j in range(c):
        #     ele = matrix[cur_r][j]

        #     a = 1
        #     b = 1

        #     while cur_r + a < r and j + b < c:
        #         if matrix[cur_r + a][j + b] != ele:
        #             return False
        #         a += 1
        #         b += 1
        
        # cur_c = 0
        # for i in range(r):
        #     ele = matrix[i][0]

        #     a = 1
        #     b = 1

        #     while i + a < r and cur_c + b < c:
        #         if matrix[i + a][cur_c + b] != ele:
        #             return False
        #         a += 1
        #         b += 1
        
        # return True


        '''
        Pattern - Matrix Traversal

        TC - O(r*c)
        SC - O(1)
        '''

        r = len(matrix)
        c = len(matrix[0])

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        
        return True
