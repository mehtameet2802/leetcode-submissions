class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)

        i = 0
        current = 0
        next = 0

        cnt = 0

        while current < time:

            while i<n and clips[i][0] <= current:
                next = max(next, clips[i][1])
                i += 1
            
            if next == current:
                return -1
            
            cnt += 1
            current = next

        return cnt