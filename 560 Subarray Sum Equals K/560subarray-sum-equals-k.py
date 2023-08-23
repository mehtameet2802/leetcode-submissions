class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = []
        pre.append(nums[0])
        cnt=0
        d1 = {}
        d1[0] = 1
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])
        
        print(pre)
        for i in range(len(pre)):
            z = pre[i]-k
            if z in d1:
                cnt+=d1[z]
            
            if pre[i] in d1:
                d1[pre[i]]+=1
            else:
                d1[pre[i]] = 1
        return cnt
