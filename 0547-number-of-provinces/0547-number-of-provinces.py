class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        cnt = 0

        def helper(i):
            nonlocal cnt

            visited.add(i)

            for j in range(len(isConnected)):
                if i == j or j in visited:
                    continue
                elif isConnected[i][j] == 1:
                    helper(j)


        for a in range(len(isConnected)):
            for b in range(len(isConnected[0])):
                if b not in visited and isConnected[a][b] == 1:
                    cnt += 1
                    helper(b)

        return cnt

            