class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        target = sum(apple)

        capacity.sort(reverse = True)

        cur_capacity = 0

        for i,c in enumerate(capacity):
            cur_capacity += c

            if cur_capacity >= target:
                return i+1
        
        return 0