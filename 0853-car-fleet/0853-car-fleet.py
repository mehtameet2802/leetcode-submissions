class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Required output: - number of car fleets
        Brute force: - calculate time and for each car check with all other cars if time is greater than of equal to, if found then they merge and become a car fleet
        Key state:
        Invariant:
        Dangerous case:
        Pseudocode: -
        sort the cars based on position in reverse order
        calculate the diff in target and siarting point, using the diff as dist calculate time taken to reach dst
        then create a stack, if empty push the time of cur ele in stack, if not empty or stack top time >= cur ele time do not push as the cars will merge and create a fleet, else push in the stack
        in the end return len of stack
        Complexity: - TC - O(n logn), SC - o(n) - time array
        '''

        time = [(start_pos,start_speed) for start_pos,start_speed in zip(position,speed)]

        time.sort(key = lambda x: -x[0])
        stack = []
        
        time = [(target-start_pos)/start_speed for start_pos, start_speed in time]

        for ele_time in time:
            if not stack:
                stack.append(ele_time)
                continue
            
            if stack[-1] < ele_time:
                stack.append(ele_time)

        return len(stack)

