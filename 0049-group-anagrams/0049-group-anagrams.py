class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        k_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            k_map[key].append(word)
        
        ans = []
        for key, item in k_map.items():
            ans.append(item)
        
        return ans