class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ans = [first]
        cur = first

        for num in encoded:
            cur = cur ^ num
            ans.append(cur)
        
        return ans
