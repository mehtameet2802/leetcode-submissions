class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        Pattern - Matrix Traversal

        TC - O(r*c)
        SC - O(r*c), O(1)
        '''
        
        r = len(mat)
        c = len(mat[0])

        i = 0
        j = 0
        direction = 1

        ans = []

        for _ in range(r*c):
            ans.append(mat[i][j])
            if direction == 1:
                
                if j == c-1:
                    i += 1
                    direction = -1
                elif i == 0:
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            
            else:
                if i == r-1:
                    j += 1
                    direction = 1
                elif j == 0:
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1
        
        return ans