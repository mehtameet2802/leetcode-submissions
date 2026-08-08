class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        for i, ch in enumerate(expression):
            if ch in "*+-":

                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for l in left:
                    for r in right:
                        if ch == '+':
                            ans.append(l+r)
                        elif ch == '-':
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
                
        if not ans:
            ans.append(int(expression))

        return ans