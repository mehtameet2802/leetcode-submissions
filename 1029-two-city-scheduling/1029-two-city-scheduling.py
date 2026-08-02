class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        '''
        Pattern - Greedy

        TC - O(N logN)
        SC - O(N)
        '''
        
        diff = [0]*len(costs)

        for i, ele in enumerate(costs):
            a = ele[0]
            b = ele[1]
            costs[i] = (ele[0]-ele[1],a,b)
        
        costs.sort(key=lambda x:x[0])

        cost = 0
        n = len(costs)//2
        for i, ele in enumerate(costs):
            if i < n:
                cost += ele[1]
            else:
                cost += ele[2]
        
        return cost