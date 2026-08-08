class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur_ele = 1
        i = 0
        ans = []

        while cur_ele <= n and i<len(target):
            if target[i] == cur_ele:
                ans.append("Push")
                i += 1
            else:
                ans.append("Push")
                ans.append("Pop")

            cur_ele += 1
        
        return ans