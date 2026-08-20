class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        values = preorder.split(",")

        slots = 1

        for val in values:
            slots -= 1
            
            if slots < 0:
                return False
            
            if val != "#":
                slots += 2
        
        return slots == 0