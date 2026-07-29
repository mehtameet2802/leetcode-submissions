class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # """
        # Pattern - Use space to reduce time

        # TC - O(m.nlogn)
        # SC - O(mn)
        # """


        # k_map = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     k_map[key].append(word)
        
        # ans = []
        # for key, item in k_map.items():
        #     ans.append(item)
        
        # return ans



        """
        Pattern - Use space to reduce time

        TC - O(m.n)
        SC - O(mn)
        """


        k_map = defaultdict(list)

        for word in strs:
            key = [0] * 26

            for ch in word:
                key[ord(ch) - ord('a')]+=1
            
            k_map[tuple(key)].append(word)
        
        return list(k_map.values())