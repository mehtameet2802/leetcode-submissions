class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
    
        if not nums:
            return []
            
        s = nums[0]

        ans = []

        i = 1
        while i < len(nums):
            if nums[i] - nums[i-1] > 1:
                e = nums[i-1]
                if s == e:
                    ans.append(str(s))
                else:
                    ans.append(f"{s}->{e}")
                s = nums[i]
            
            i+=1

        e = nums[len(nums)-1]
        if s == e:
            ans.append(str(s))
        else:
            ans.append(f"{s}->{e}")
        
        return ans
            
