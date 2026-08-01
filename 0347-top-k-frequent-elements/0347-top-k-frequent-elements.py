from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = Counter(nums)

        ans = []

        for val, f in sorted(f_map.items(),key=lambda x:x[1], reverse=True):
            if k>0:
                ans.append(val)
                k-=1
            else:
                break
        
        return ans

