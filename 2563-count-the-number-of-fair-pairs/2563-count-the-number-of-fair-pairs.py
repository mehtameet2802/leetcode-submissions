class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        Pattern - Sort + Lower Bound + Upper Bound

        Idea:
        1. Sort the array.
        2. Fix one element nums[i].
        3. Find all valid partners in the suffix (i+1 ... n-1).
        4. The partner must satisfy:

        lower - nums[i] <= partner <= upper - nums[i]

        5. Use:
        - Lower Bound for (lower - nums[i])
        - Upper Bound for (upper - nums[i])

        6. Count = upper_bound - lower_bound

        TC - O(N log N)
            - Sorting: O(N log N)
            - N iterations × 2 binary searches: O(N log N)

        SC - O(1)
            (Ignoring the sorting algorithm's auxiliary space.
            Python's built-in sort (Timsort) uses O(N) extra space.)
        '''

        nums.sort()

        ans = 0
        for i,num in enumerate(nums):
            left = lower - num
            right = upper - num

            l = bisect_left(nums, left, i+1)
            r = bisect_right(nums, right, i+1)

            ans += (r-l)
        
        return ans