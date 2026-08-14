class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_map = defaultdict(int)
        in_map = defaultdict(int)

        if n == 1:
            return n

        for a,b in trust:
            out_map[a] += 1
            in_map[b] += 1
        
        for val, f in in_map.items():
            if f == n-1:
                if out_map[val] == 0:
                    return val
            
        return -1