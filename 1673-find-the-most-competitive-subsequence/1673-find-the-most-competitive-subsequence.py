class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        remove = len(nums) - k
        stack = []

        for num in nums:
            while stack and stack[-1] > num and remove > 0:
                stack.pop()
                remove -= 1
            
            stack.append(num)
        
        return stack[:k]