class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid < 0:
                state = False
                while stack and stack[-1] > 0:
                    ele = stack.pop()

                    if ele > abs(asteroid):
                        stack.append(ele)
                    
                    if ele >= abs(asteroid):
                        state = True
                        break
                    
                
                if state:
                    continue
            
            stack.append(asteroid)

        return stack
                    