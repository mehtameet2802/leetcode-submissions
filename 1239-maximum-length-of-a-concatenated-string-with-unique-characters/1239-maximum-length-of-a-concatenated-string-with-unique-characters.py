class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        used = set()

        def helper(i):
            nonlocal ans

            ans = max(ans, len(used))

            for j in range(i, len(arr)):

                if len(set(arr[j])) != len(arr[j]):
                    continue
                
                if set(arr[j]) & used:
                    continue

                used.update(arr[j])

                helper(j+1)

                for ch in arr[j]:
                    used.remove(ch)
        
        helper(0)
        return ans