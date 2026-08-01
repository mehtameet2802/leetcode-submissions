class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0]*len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                self.pre_sum[0] = nums[0]
                continue
            
            self.pre_sum[i] = nums[i] + self.pre_sum[i-1]
        
        print(self.pre_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pre_sum[right]
        return self.pre_sum[right]-self.pre_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)