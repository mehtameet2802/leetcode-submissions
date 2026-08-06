from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Pattern - Custom Comparator Sort

        TC - O(n log n * k)
        SC - O(n)

        n = number of elements
        k = average number of digits
        '''

        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1      # a should come first
            elif a + b < b + a:
                return 1       # b should come first
            return 0

        nums.sort(key=cmp_to_key(compare))

        ans = "".join(nums)

        # Handle cases like [0,0]
        return "0" if ans[0] == "0" else ans