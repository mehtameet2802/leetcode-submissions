class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)

        verticalCuts.append(0)
        verticalCuts.append(w)

        verticalCuts.sort()
        horizontalCuts.sort()

        max_h = 0
        max_w = 0

        for i in range(1,len(horizontalCuts)):
            cur_h = horizontalCuts[i] - horizontalCuts[i-1]

            max_h = max(max_h,cur_h)

        
        for i in range(1,len(verticalCuts)):
            cur_w = verticalCuts[i] - verticalCuts[i-1]
            max_w = max(max_w,cur_w)
        
        return (max_w*max_h)%(pow(10,9)+7)