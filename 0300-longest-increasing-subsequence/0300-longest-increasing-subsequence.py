class Solution:
    # def lengthOfLIS(self, nums: list[int]) -> int:

    #     # Required output: - max LIS
    #     # Brute-force choices:
    #     # Recursive state:
    #     # What does solve(...) return? - it returns max LIS that can be acheived if we take the current value or skip it
    #     # What information determines whether nums[i] can be taken? - pre_idx == -1 or nums[i] > nums[pre_idx]:
    #     # Base case: - if i>=n:
    #     #         return 0
    #     # Recurrence:
    #     # Memoized TC and SC:
        
    #     n = len(nums)
    #     def solve(i, pre_idx):
    #         if i>=n:
    #             return 0
            
    #         skip = solve(i+1, pre_idx)

    #         take = 0
    #         if pre_idx == -1 or nums[i] > nums[pre_idx]:
    #             take = 1 + solve(i+1, i)
            
    #         return max(skip,take)

    #     return solve(0,-1)


    # def lengthOfLIS(self, nums: list[int]) -> int:

    #     # Required output: - max LIS
    #     # Brute-force choices:
    #     # Recursive state:
    #     # What does solve(...) return? - it returns max LIS that can be acheived if we take the current value or skip it
    #     # What information determines whether nums[i] can be taken? - pre_idx == -1 or nums[i] > nums[pre_idx]:
    #     # Base case: - if i>=n:
    #     #         return 0
    #     # Recurrence:
    #     # Memoized TC and SC: - TC - O(n^2), SC- O(n^2) + O(n)
        
    #     n = len(nums)
    #     dp = {}
    #     def solve(i, pre_idx):
    #         if i>=n:
    #             return 0
            
    #         state = (i,pre_idx)

    #         if state in dp:
    #             return dp[state]

    #         skip = solve(i+1, pre_idx)

    #         take = 0
    #         if pre_idx == -1 or nums[i] > nums[pre_idx]:
    #             take = 1 + solve(i+1, i)
            
    #         dp[state] = max(skip,take)
    #         return dp[state]

    #     return solve(0,-1)


    def lengthOfLIS(self, nums: list[int]) -> int:

        # Required output: - max LIS
        # Brute-force choices:
        # Recursive state:
        # What does solve(...) return? - it returns max LIS that can be acheived if we take the current value or skip it
        # What information determines whether nums[i] can be taken? - pre_idx == -1 or nums[i] > nums[pre_idx]:
        # Base case: - if i>=n:
        #         return 0
        # Recurrence:
        # Memoized TC and SC: - TC - O(n^2), SC- O(n^2) + O(n)
        
        tail = []
        n = len(nums)
        for i in range(n):
            left = bisect_left(tail, nums[i])

            if left == len(tail):
                tail.append(nums[i])
            else:
                tail[left] = nums[i]

        return len(tail)