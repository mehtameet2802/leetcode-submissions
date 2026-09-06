class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        binary search on weight capacity of the ship

        l = max(weights)
        right = sum(weights)

        need function possible - 
        it takes weight capacity
        for each weight capacity it calculates days taken to ship all the wights
        if days_taken <= days return True, else False

        when possible is True - right = mid
        else left = mid + 1
        '''

        def possible(capacity):
            days_taken = 0
            cur_capacity = capacity
            for weight in weights:
                if weight > cur_capacity:
                    cur_capacity = capacity
                    days_taken += 1
                
                cur_capacity -= weight
            
            days_taken += 1
            print(capacity, days_taken)
            return days_taken <= days
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left)//2

            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
