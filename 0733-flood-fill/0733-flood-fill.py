class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        cur_color = image[sr][sc]

        if cur_color == color:
            return image

        def helper(r,c):
            
            image[r][c] = color
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or image[nr][nc]!=cur_color:
                    continue
                
                helper(nr,nc)
        
        helper(sr, sc)
        image[sr][sc] = color
        return image