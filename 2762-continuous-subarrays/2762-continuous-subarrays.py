class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        '''
        Pattern - Variable Sliding Window + Deque

        TC - O(N)
        SC - O(N)
        '''

        minQ = deque([])
        maxQ = deque([])

        left = 0
        ans = 0

        for right in range(len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()
            
            maxQ.append(right)
        
            while minQ and nums[minQ[-1]] > nums[right]:
                minQ.pop()
            
            minQ.append(right)

            while nums[maxQ[0]] - nums[minQ[0]] < 0 or nums[maxQ[0]] - nums[minQ[0]] > 2:
                if maxQ[0] == left:
                    maxQ.popleft()
                
                if minQ[0] == left:
                    minQ.popleft()
                
                left += 1
            
            ans += (right - left + 1)
        
        return ans
