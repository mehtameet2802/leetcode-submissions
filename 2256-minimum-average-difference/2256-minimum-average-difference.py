class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        cur = float('inf')
        pre_sum = 0
        total = sum(nums)
        n = len(nums)

        for i, num in enumerate(nums):
            # if num == 0:
            #     diff
            #     continue
            
            pre_sum += num
            avg1 = pre_sum//(i+1)
            

            if i == n-1:
                avg2 = 0
            else:
                avg2 = (total - pre_sum)//(n-i-1)
            
            diff = abs(avg1 - avg2)
            if diff < cur:
                cur = diff
                ans = i
            
        
        return ans

