class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for opt in operations:
            if opt == "--X" or opt == "X--":
                val -= 1
            else:
                val += 1
        
        return val