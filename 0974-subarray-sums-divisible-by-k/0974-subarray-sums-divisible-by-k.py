class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        remainders[0] += 1

        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            ans += remainders[remainder]

            remainders[remainder] += 1

        return ans
