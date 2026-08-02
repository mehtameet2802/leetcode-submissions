class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        p_map = defaultdict(int)

        for i,ch in enumerate(s):
            p_map[ch] = i
        
        ans = []
        max_idx = p_map[s[0]]
        start = 0
        
        i = 0
        while i<len(s):
            if i == max_idx:
                ans.append(max_idx-start+1)
                start = max_idx+1

                if max_idx+1 < len(s):
                    max_idx = p_map[s[max_idx+1]]
            elif p_map[s[i]] > max_idx:
                max_idx = p_map[s[i]]
            i+=1

        return ans
            

