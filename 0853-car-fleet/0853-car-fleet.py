class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        times = [(start_pos, start_speed) for start_pos, start_speed in zip(position,speed)]

        times.sort(key = lambda x : -x[0])


        for idx, ele in enumerate(times):
            start_pos = ele[0]
            start_speed = ele[1]
            times[idx] = (target-start_pos)/start_speed
        
        stack = []


        for time in times:

            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)
