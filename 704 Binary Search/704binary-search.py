class Solution:
    ans = -1
    def bin(self,s,e,arr,k):
        mid = int(s+(e-s)//2)
        if mid>=e:
            self.ans=-1
        elif arr[mid]==k:
            self.ans = mid
        elif s==mid:
            self.ans = -1
        elif arr[mid]<k:
            self.bin(mid+1,e,arr,k)
        elif arr[mid]>k:
            self.bin(s,mid,arr,k)

    def search(self, nums: List[int], target: int) -> int:
        self.bin(0,len(nums),nums,target)
        return self.ans
