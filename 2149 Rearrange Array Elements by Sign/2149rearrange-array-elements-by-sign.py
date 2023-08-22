class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n1 = []
        n2 = []
        for item in nums:
            if item<0:
                n2.append(item)
            else:
                n1.append(item)
        
        s1 = 0
        s2 = 0
        cur = 0
        while s1<len(n1) and s2<len(n2):
            if cur%2==0:
                nums[cur] = n1[s1]
                s1+=1
            else:
                nums[cur] = n2[s2]
                s2+=1
            cur+=1
        
        while s1<len(n1):
            nums[cur] = n1[s1]
            s1+=1
            cur+=1
        
        while s2<len(n2):
            nums[cur] = n2[s2]
            s2+=1
            cur+=1

        return nums