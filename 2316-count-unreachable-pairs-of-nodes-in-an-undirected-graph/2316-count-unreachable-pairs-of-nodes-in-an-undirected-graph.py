class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        '''
        Required output: number of pairs of unreachable nodes

        What makes two nodes reachable? - either the nodes are connected directly or via some other node

        What information is needed from each connected component? - 

        Brute-force approach:

        Why will brute force fail?

        Pattern prediction: Floyd Warshall

        What does the traversal/helper return? 

        How will visited nodes be handled?

        How can component sizes produce the answer
        without checking every pair?

        Invariant:

        Expected TC and SC:

        Dangerous cases:
        '''



        '''
        Corrected Thought
        Required output: number of pairs of unreachable nodes

        What makes two nodes reachable? - either the nodes are connected directly or via some other node

        What information is needed from each connected component? - number of nodes in each component

        Brute-force approach:

        Why will brute force fail?

        Pattern prediction: DFS

        What does the traversal/helper return? - no of nodes in the component 

        How will visited nodes be handled? using a visited set

        How can component sizes produce the answer
        without checking every pair? - we know number of nodes in each component then we can get all possible pair which cannot exist as the nodes are not part of the same component by multiplying the number of node

        Invariant:

        Expected TC and SC:

        Dangerous cases:
        '''

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        nodes_arr = []
        visited = set()

        def helper(node):
            visited.add(node)

            cnt = 0
            for nei in graph[node]:
                if nei in visited:
                    continue

                cnt += helper(nei)
            
            return cnt + 1

        for node in range(n):
            if node not in visited:
                nodes_arr.append(helper(node))
        
        nodes_arr.sort()

        ans = 0
        # for i in range(len(nodes_arr)):
        #     for j in range(i+1,len(nodes_arr)):
        #         ans += nodes_arr[i]*nodes_arr[j]

        remaining = n
        for component_size in nodes_arr:
            remaining -= component_size
            ans += component_size * remaining

        return ans


        
