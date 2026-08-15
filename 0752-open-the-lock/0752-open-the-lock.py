class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        queue = deque([("0000",0)])
        visited = {"0000"}

        while queue:
            combination, cnt = queue.popleft()

            if combination == target:
                return cnt

            for i, wheel in enumerate(combination):
                digit = int(wheel)
                for next_digit in [(digit + 1)%10,(digit-1)%10]:
                    
                    code = list(combination)
                    code[i] = str(next_digit)
                    code = "".join(code)

                    if code in deadends or code in visited:
                        continue

                    visited.add(code)
                    queue.append((code,cnt+1))
            
        return -1
                    


