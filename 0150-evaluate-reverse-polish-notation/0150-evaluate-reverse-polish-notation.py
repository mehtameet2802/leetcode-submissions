class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        opt = {
            '+': lambda a,b : a+b,
            '-': lambda a,b : a-b,
            '/': lambda a,b : int(a/b),
            '*': lambda a,b : a*b,
        }

        for token in tokens:
            if token in opt:
                ele1 = stack.pop()
                ele2 = stack.pop()
                stack.append(opt[token](ele2,ele1))
                print(stack[-1])
            else:
                stack.append(int(token))


        return stack[-1]