import random

class RandomizedSet:

    # """
    # Pattern - Use space to reduce time

    # TC - O(1) - for first 2, O(n) - for last 1
    # SC - O(n)

    # """


    # def __init__(self):
    #     self.seen = set()

    # def insert(self, val: int) -> bool:
    #     if val in self.seen:
    #         return False
        
    #     self.seen.add(val)
    #     return True
        

    # def remove(self, val: int) -> bool:
    #     if val not in self.seen:
    #         return False
        
    #     self.seen.remove(val)
    #     return True
        

    # def getRandom(self) -> int:
    #     return random.choice(list(self.seen))


    
    # Optimized
    """
    Pattern - Use space to reduce time

    TC - O(1) - for first all 3
    SC - O(n)

    """


    def __init__(self):
        self.arr = []
        self.e_map = {}

    def insert(self, val: int) -> bool:
        if val in self.e_map:
            return False
        
        self.arr.append(val)
        self.e_map[val] = len(self.arr)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.e_map:
            return False
        
        ind = self.e_map[val]
        self.e_map.pop(val)
        self.arr.remove(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()