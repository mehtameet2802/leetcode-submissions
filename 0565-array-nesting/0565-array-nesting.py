class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        '''
        Pattern - Graph or Cyclic Traversal

        TC - O(N)
        SC - O(N)
        '''

        ans = 0

        for i in range(len(nums)):
            if nums[i] != -1:
                cur = i
                length = 0
                while nums[cur] != -1:
                    next = nums[cur]
                    nums[cur] = -1
                    cur = next
                    length += 1
                ans = max(ans, length)
            

        return ans