class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stack = []
        
        for idx, height in enumerate(heights):
            while stack and stack[-1][0] >= height:
                ele_height, ele_idx = stack.pop()

                if stack:
                    left_idx = stack[-1][1]
                else:
                    left_idx = -1
            
                right_idx = idx

                area = (right_idx-left_idx-1)*ele_height
                max_area = max(area, max_area)

            stack.append((height, idx))

        while stack:
            ele_height, ele_idx = stack.pop()

            if stack:
                left_idx = stack[-1][1]
            else:
                left_idx = -1
        
            right_idx = len(heights)

            area = (right_idx-left_idx-1)*ele_height
            max_area = max(area, max_area)
        
        return max_area

