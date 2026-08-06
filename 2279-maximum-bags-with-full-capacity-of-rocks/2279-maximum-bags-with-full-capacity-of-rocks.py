class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        '''
        Pattern - Sort + Greedy

        TC - O(N log N)
        SC - O(1)
        '''

        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        
        capacity.sort()

        for i in range(len(capacity)):
            if capacity[i] == 0:
                continue
            
            if capacity[i] <= additionalRocks:
                additionalRocks -= capacity[i]
            else:
                return i
        
        return len(capacity)

