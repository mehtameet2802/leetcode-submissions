class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        l = 0
        r = len(people)-1

        cnt = 0

        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            elif people[r]<=limit:
                r-=1
            
            cnt+=1
        
        return cnt