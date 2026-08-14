class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def helper(r,c, visited):
            visited.add((r,c))

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue
                
                helper(nr,nc, visited)

        
        for i in range(COLS):
            helper(0,i,pacific)

        for i in range(ROWS):
            helper(i,0,pacific)

        for i in range(ROWS):
            helper(i,COLS-1,atlantic)

        for i in range(COLS):
            helper(ROWS-1,i,atlantic)

        ans = []
        for r,c in pacific:
            if (r,c) in atlantic:
                ans.append([r,c])

        return ans