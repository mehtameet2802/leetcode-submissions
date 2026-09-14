class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # horizontalCuts.append(0)
        # horizontalCuts.append(h)

        # verticalCuts.append(0)
        # verticalCuts.append(w)

        # boundaries = set()

        # for r in horizontalCuts:
        #     for c in verticalCuts:
        #         boundaries.add((r,c))
        
        # print(boundaries)

        # dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        # visited = set()
        # ROWS = h
        # COLS = w
        # area = 0
        
        # def helper(r,c,l,h):
        #     nonlocal area

        #     visited.add((r,c))

        #     if (r,c) in boundaries:
        #         area = max(area, l*h)

        #         l = 0
        #         h = 0

        #     for dr,dc in dirs:
        #         nr = r + dr
        #         nc = c + dc

        #         if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
        #             continue
                
        #         if (nr,nc) in visited:
        #             continue
                
        #         helper(nr,nc,l+dc,h+dr)

        # visited.add((0,0))
        # helper(0,0,0,0)

        # return area

        horizontalCuts.append(0)
        horizontalCuts.append(h)

        verticalCuts.append(0)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        max_h = 0
        max_w = 0

        for i in range(1,len(horizontalCuts)):
            cur_h = horizontalCuts[i] - horizontalCuts[i-1]
            max_h = max(max_h, cur_h)

        for j in range(1, len(verticalCuts)):
            cur_w = verticalCuts[j] - verticalCuts[j-1]
            max_w = max(max_w, cur_w)

        return (max_h*max_w)%(pow(10,9)+7)
