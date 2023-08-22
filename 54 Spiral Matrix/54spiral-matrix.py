class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        sr,sc,er,ec = 0,0,m,n
        cnt = 0
        tnt = m*n

        while cnt<tnt:
            r = sr
            c = sc
            while c<ec and cnt<tnt:
                ans.append(matrix[r][c])
                cnt+=1
                c+=1
            c-=1
            r+=1
            while r<er and cnt<tnt:
                ans.append(matrix[r][c])
                cnt+=1
                r+=1
            r-=1
            c-=1
            while c>sc and cnt<tnt:
                ans.append(matrix[r][c])
                cnt+=1
                c-=1
            
            while r>sr and cnt<tnt:
                ans.append(matrix[r][c])
                cnt+=1
                r-=1
            
            sr+=1
            sc+=1
            er-=1
            ec-=1

    
        return ans
