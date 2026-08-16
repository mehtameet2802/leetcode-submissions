class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        '''
        TC = O(N × 2^N)
        SC = O(N)
        '''
        ans = 0
        path = []

        def helper(i):
            nonlocal ans

            if path:
                ans += 1

            for j in range(i, len(nums)):
                # Take nums[i] if valid
                if nums[j] - k not in path and nums[j] + k not in path:
                    path.append(nums[j])
                    helper(j + 1)
                    path.pop()

        helper(0)
        return ans