class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opt in operations:
            if opt == "C":
                stack.pop()
            elif opt == "D":
                ele1 = stack[-1]
                stack.append(ele1*2)
            elif opt == "+":
                ele1 = stack[-1]
                ele2 = stack[-2]
                stack.append(ele1 + ele2)
            else:
                stack.append(int(opt))

        print(stack)

        return sum(stack) if stack else 0