class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        Pattern - Use space to reduce time

        TC - O(n)
        SC - O(n)
        """

        seen = set()
        
        for num in nums:
            seen.add(num)
        
        ans = 0
        for num in seen:
            if num-1 in seen:
                continue
            
            next = num+1
            length = 1
            while next in seen:
                next = next+1
                length += 1
            
            ans = max(ans,length)
        
        return ans


        