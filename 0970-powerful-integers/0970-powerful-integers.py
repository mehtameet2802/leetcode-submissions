class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        ans = set()

        p_x = 1
        while p_x <= bound:
            p_y = 1

            while p_x + p_y <= bound:
                ans.add(p_x + p_y)

                if y == 1:
                    break
                
                p_y = p_y*y
            
            if x == 1:
                break
            
            p_x = p_x*x

        return list(ans)

