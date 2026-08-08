class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        Pattern - BInary Search on Answer

        TC - O(N log N)
        SC - O(1)
        '''

        if m*k > len(bloomDay):
            return -1
        
        def can(day):
            flowers = 0
            bouqets = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouqets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return bouqets >= m


        start = min(bloomDay)
        end = max(bloomDay)

        while start < end:
            mid = start + (end - start) // 2

            if can(mid):
                end = mid
            else:
                start = mid + 1
            
        return start