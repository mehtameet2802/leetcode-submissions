class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = defaultdict(int)

        dirs = [[0,1],[1,0]]

        def helper(r,c):
            if (r,c) in seen:
                return seen[(r,c)]
            
            if r==m-1 and c==n-1:
                return 1

            paths = 0
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=m or nc>=n:
                    continue
                
                paths += helper(nr,nc)

            seen[(r,c)] = paths
            
            return paths
        
        return helper(0,0)
        
            
