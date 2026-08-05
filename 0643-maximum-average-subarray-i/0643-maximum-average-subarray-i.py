class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = 0
        total = 0
        ans = -float('inf')

        for right in range(len(nums)):
            total += nums[right]

            if right - left + 1 == k:
                
                avg = total / k
                ans = max(ans,avg)

                total -= nums[left]
                
                left += 1

        return ans