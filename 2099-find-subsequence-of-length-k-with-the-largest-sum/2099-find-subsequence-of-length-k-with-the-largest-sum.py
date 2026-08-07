class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        f_map = defaultdict(int)
        temp = sorted(nums)

        ans = []
        i = len(nums)-1
        while k>0:
            f_map[temp[i]] += 1
            k -= 1
            i -= 1
        
        for num in nums:
            if num in f_map and f_map[num]>0:
                ans.append(num)
                f_map[num] -= 1

        return ans

