class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ch_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        path = []
        ans = []

        def helper(i):
            if i == len(digits):
                ans.append("".join(path))
                return
            
            for ch in ch_map[digits[i]]:
                path.append(ch)
                helper(i+1)
                path.pop()
            
        helper(0)
        return ans
