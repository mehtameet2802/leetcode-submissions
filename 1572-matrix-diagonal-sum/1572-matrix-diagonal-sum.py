class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        # '''
        # Pattern - Matrix Traversal
        
        # TC - O(N)
        # SC - O(1)
        # '''

        # ans = 0
        # r = len(mat)
        # c = len(mat[0])

        # i = j = 0
        # while i < r:
        #     ans += mat[i][j]
        #     i += 1
        #     j += 1
        
        # i = 0
        # j = c-1
        # while i < r:
        #     if i == j:
        #         i += 1
        #         j -= 1
        #         continue
        #     ans += mat[i][j]
        #     i += 1
        #     j -= 1
        
        # return ans



        '''
        Pattern - Matrix Traversal
        
        TC - O(N)
        SC - O(1)
        '''

        ans = 0
        r = len(mat)

        for i in range(r):
            ans += mat[i][i]
            ans += mat[i][r-i-1]
            i += 1

        if i%2 != 0:
            ans -= mat[r//2][r//2]
     
        return ans