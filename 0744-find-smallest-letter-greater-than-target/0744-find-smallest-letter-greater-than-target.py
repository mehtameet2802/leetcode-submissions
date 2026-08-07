class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        Pattern - Upper BOund
        TC - O(log N)
        SC - O(1)
        '''
        r = bisect_right(letters, target)
        if r == len(letters):
            return letters[0]
        
        return letters[r]