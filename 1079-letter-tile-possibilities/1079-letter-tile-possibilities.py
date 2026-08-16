class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        ans = 0
        path = []
        seen = set()

        def helper():
            nonlocal ans

            if path:
                ans += 1
            
            for i in range(len(tiles)):
                if i in seen:
                    continue

                if i>0 and tiles[i] == tiles[i-1] and i-1 not in seen:
                    continue
                
                seen.add(i)
                path.append(tiles[i])
                helper()
                path.pop()
                seen.remove(i)
        
        helper()
        return ans