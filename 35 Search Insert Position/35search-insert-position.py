class Solution:
    ans = -1
    def bin(self,s,e,arr,k):
        mid = int(s+(e-s)//2)
        if arr[mid]==k:
            self.ans = mid
        elif s==mid:
            if arr[mid]>k:
                self.ans = mid
            else:
                self.ans = mid+1
        elif arr[mid]>k:
            self.bin(s,mid,arr,k)
        elif arr[mid]<k:
            self.bin(mid+1,e,arr,k)

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target>nums[n-1]:
            return n
        self.bin(0,n,nums,target)
        return self.ans