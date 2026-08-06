class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # '''
        # Pattern - Sort + Greedy

        # TC - O(n log n)
        # SC - O(1)
        # '''

        # if sum(costs) < coins:
        #     return len(costs)

        # costs.sort()

        # if costs[0] > coins:
        #     return 0
        
        # cur = 0
        # for i, cost in enumerate(costs):
        #     cur += cost
        #     if cur > coins:
        #         return i

        # return len(costs)

        '''
        Pattern - Counting Sort

        TC - O(n)
        SC - O(1)
        '''

        freq = [0]*100001
        ans = 0

        for cost in costs:
            freq[cost] += 1

        for cost, _ in enumerate(freq):
            
            while freq[cost]>0 and coins >= cost:
                coins -= cost
                freq[cost] -= 1
                ans += 1
        
        return ans