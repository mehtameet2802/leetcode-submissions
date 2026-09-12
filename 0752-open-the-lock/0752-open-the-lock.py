class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        '''
        Required output: minimum operations to get to target
        Brute-force idea: 
        Pattern prediction: BFS
        What does one state represent?  - it represents combination of the lock
        How are valid next states generated? - for each state, have a for loop of range 4, wheel at each index will either go +1 or -1 and generate a new state also do modulo 10 for the wrap around
        Which states are forbidden?  - the states that are in deadends
        How will repeated states be prevented? -  maintain a visited set
        What makes the returned result optimal? - we use bfs and in that all the combinations acheived in a particular number of operations, are stored together in the queue, so this ensures that the target is found in min number of operations 
        When should a state be marked visited? - in visited set add the combination
        Invariant:
        Expected TC and SC: TC -  SC - 
        '''

        if "0000" in deadends or target in deadends:
            return -1

        queue = deque()
        queue.append(("0000",0))
        visited = set()
        visited.add("0000")
        deadends = set(deadends)

        while queue:
            length = len(queue)

            for _ in range(length):
                state, opt = queue.popleft()

                if state == target:
                    return opt

                for idx in range(4):
                    new_state1 = state[:idx] + str((int(state[idx])+1)%10) + state[idx+1:]
                    new_state2 = state[:idx] + str((int(state[idx])-1)%10) + state[idx+1:]

                    if new_state1 == target or new_state2 == target:
                        return opt + 1
                    
                    if new_state1 not in deadends and new_state1 not in visited:
                        visited.add(new_state1)
                        queue.append((new_state1,opt+1))

                    if new_state2 not in deadends and new_state2 not in visited:
                        visited.add(new_state2)
                        queue.append((new_state2,opt+1))

        return -1

