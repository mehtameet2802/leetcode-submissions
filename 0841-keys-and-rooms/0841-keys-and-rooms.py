class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        TC = O(V + E)
        SC - O(V)
        '''

        stack = [0]
        visited = set()

        while stack:
            room = stack.pop()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        
        return True if len(visited) == len(rooms) else False
