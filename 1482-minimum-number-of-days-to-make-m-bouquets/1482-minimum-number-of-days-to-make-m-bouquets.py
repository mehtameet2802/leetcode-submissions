class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        if m*k > len(bloomDay):
            return -1
        
        def possible(val):
            bouquet = 0
            adjacency = 0

            for day in bloomDay:
                if day <= val:
                    adjacency += 1

                    if adjacency == k:
                        bouquet += 1
                        adjacency = 0

                        if bouquet >= m:
                            return True
                else:
                    adjacency = 0

            return False


        right = max(bloomDay)
        left = min(bloomDay)

        while left < right:
            mid = left + (right - left )//2

            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        

