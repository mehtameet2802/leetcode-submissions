class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = defaultdict(list)
        remainders[0].append(-1)

        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if len(remainders[remainder])>0:
                if idx - remainders[remainder][0] >= 2:
                    return True
                    
            remainders[remainder].append(idx)

        return False