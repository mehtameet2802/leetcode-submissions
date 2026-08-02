class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = 1
        ans = max_prod = min_prod = nums[0] 

        for num in nums[1:]:
            min_prod, max_prod = min(num, num*min_prod, num*max_prod), max(num, num*min_prod, num*max_prod)
            
            ans = max(ans,max_prod)
            
        return ans