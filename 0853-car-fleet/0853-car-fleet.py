class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:

        # Stack stores the arrival time of each fleet.
        #
        # We process cars from:
        # closest to target  --->  farthest from target
        #
        # Example:
        # target = 12
        # positions = [10, 8, 5, 3, 0]
        #
        # The car at 10 is in front of the car at 8,
        # which is in front of the car at 5, etc.
        stack = []

        # We must pair each position with its speed.
        #
        # Then sort by position in descending order.
        #
        # reverse=True means:
        #
        # position 10
        # position 8
        # position 5
        # position 3
        # position 0
        #
        # So we process the car closest to the target first.
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:

            # Time required for this car to reach target
            #
            # distance = target - pos
            # time = distance / speed
            time = (target - pos) / spd

            # If there is no fleet yet,
            # this car automatically creates the first fleet.
            #
            # Otherwise, compare this car's arrival time
            # with the fleet immediately in front of it.
            #
            # IMPORTANT:
            #
            # If:
            #
            #       time <= stack[-1]
            #
            # this car is faster than or equal to the fleet ahead.
            #
            # Therefore, it will catch that fleet.
            #
            # Example:
            #
            # front fleet = 7 hours
            # current car  = 3 hours
            #
            # The current car would arrive in 3 hours
            # if it could travel independently.
            #
            # But it cannot pass the fleet.
            # Therefore, it catches the fleet and becomes
            # part of that fleet.
            #
            # We DO NOT add 3 to the stack.
            #
            # The fleet still reaches the target in 7 hours
            # because the slower car/fleet determines the speed.
            #
            # If:
            #
            #       time > stack[-1]
            #
            # then this car is slower than the fleet ahead.
            #
            # Example:
            #
            # front fleet = 3 hours
            # current car = 7 hours
            #
            # The current car can never catch the fleet.
            # Therefore, it creates a NEW fleet.
            if not stack or time > stack[-1]:
                stack.append(time)

        # Every value in stack represents one fleet.
        #
        # Example:
        #
        # stack = [1, 7, 12]
        #
        # means there are 3 fleets.
        return len(stack)