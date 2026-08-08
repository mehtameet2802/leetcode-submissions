class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")

        stack = []

        for ele in arr:
            if ele == "" or ele == ".":
                continue
            elif ele == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        
        return "/" + "/".join(stack)