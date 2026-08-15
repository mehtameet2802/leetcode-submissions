class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        '''
        TC = O(6000) ≈ O(1)
        SC = O(6000) ≈ O(1)
        '''

        queue = deque([(0,"S",0)])
        visited = {(0,"F")}
        forbidden = set(forbidden)

        if 0 in forbidden:
            return -1

        while queue:
            pos, jump, jumps = queue.popleft()

            if pos == x:
                return jumps

            nf = pos + a

            if nf<=6000 and nf not in forbidden and (nf,"F") not in visited:
                visited.add((nf,"F"))
                queue.append((nf,"F",jumps+1))

            nb = pos - b

            if jump != "B" and nb>=0 and nb not in forbidden and (nb,"B") not in visited:
                visited.add((nb,"B"))
                queue.append((nb,"B",jumps+1))
                
        return -1 