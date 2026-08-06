class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []

        for c,r in zip(capacity,rocks):
            diff.append(c-r)
        
        diff.sort()

        for i in range(len(diff)):
            if diff[i] == 0:
                continue
            
            if diff[i] <= additionalRocks:
                additionalRocks -= diff[i]
            else:
                return i
        
        return len(diff)

