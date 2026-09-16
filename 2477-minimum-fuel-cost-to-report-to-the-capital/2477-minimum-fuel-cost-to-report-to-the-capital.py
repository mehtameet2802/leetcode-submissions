class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)

        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        fuel = 0
        visited = set()

        def helper(node):
            nonlocal fuel

            visited.add(node)

            people = 0
            for nei in graph[node]:
                if nei in visited:
                    continue

                people += helper(nei)
            
            if node == 0:
                return people
            people += 1
            fuel += ceil(people/seats)
            return people

        visited.add(0)
        helper(0)
        
        return fuel