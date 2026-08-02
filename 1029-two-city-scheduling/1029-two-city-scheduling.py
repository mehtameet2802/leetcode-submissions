class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        '''
        Pattern - Greedy

        TC - O(N logN)
        SC - O(1)
        '''
        
        diff = [0]*len(costs)
        
        costs.sort(key=lambda x:x[0]-x[1])

        cost = 0
        n = len(costs)//2
        for i, ele in enumerate(costs):
            if i < n:
                cost += ele[0]
            else:
                cost += ele[1]
        
        return cost