class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        r = len(boxGrid)
        c = len(boxGrid[0])

        for i in range(r):

            empty = c - 1
            for j in range(c-1,-1,-1):
                if boxGrid[i][j] == '*':
                    empty = j-1
                
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1

        
        ans = [['.']*r for _ in range(c)]

        for i in range(r):
            for j in range(c):
                ans[j][r-i-1] = boxGrid[i][j]
        
        return ans
