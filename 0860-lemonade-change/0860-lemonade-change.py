class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c_map = {
            5:0,
            10:0,
            20:0
        }

        for bill in bills:
            c_map[bill] += 1
            if bill == 20:
                if (c_map[10]>=1 and c_map[5]>=1):
                    c_map[10]-=1
                    c_map[5]-=1
                elif c_map[5]>=3:
                    c_map[5]-=3
                else:
                    return False
            elif bill == 10:
                if c_map[5]>=1:
                    c_map[5]-=1
                else:
                    return False
        
        return True
            