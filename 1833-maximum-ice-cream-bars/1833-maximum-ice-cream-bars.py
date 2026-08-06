class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        if sum(costs) < coins:
            return len(costs)

        costs.sort()

        if costs[0] > coins:
            return 0
        
        cur = 0
        for i, cost in enumerate(costs):
            cur += cost
            if cur > coins:
                return i

        return len(costs)
