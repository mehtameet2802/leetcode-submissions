class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        ele1 = -1
        ele2 = -1

        for num in nums:
            if ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = num
                cnt1+=1
            elif cnt2 == 0:
                ele2 = num
                cnt2+=1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
        
        n = len(nums)
        ans = []
        if cnt1 > n//3:
            ans.append(ele1)
        
        if cnt2 > n//3:
            ans.append(ele2)
        
        return ans