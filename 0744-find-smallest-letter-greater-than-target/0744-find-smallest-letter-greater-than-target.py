class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        r = bisect_right(letters, target)
        if r == len(letters):
            return letters[0]
        
        return letters[r]