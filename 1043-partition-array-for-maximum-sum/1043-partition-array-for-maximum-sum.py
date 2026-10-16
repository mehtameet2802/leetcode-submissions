class Solution:
    # def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
    #     # dp[index] means: - it represents the max val that can be schieved considered i is start point
    #     # Which future states does it read? - it shores states from start to min(n,start+k)
    #     # Fill direction: - forward
    #     # Which variables must reset for every index? - best and cur_max
    #     # Final return cell: - best val of that partition start and all possible end

    #     n = len(arr)
    #     def solve(start):
    #         best = 0
    #         cur_max = 0

    #         for end in range(start, min(n,start+k)):
    #             cur_max = max(cur_max, arr[end])

    #             par_len = end-start+1
    #             par_val = par_len * cur_max

    #             remaining = par_val + solve(end+1)

    #             best = max(best, remaining)
            
    #         return best
    #     return solve(0)

    # def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
    #     # dp[index] means: - it represents the max val that can be schieved considered i is start point
    #     # Which future states does it read? - it shores states from start to min(n,start+k)
    #     # Fill direction: - forward
    #     # Which variables must reset for every index? - best and cur_max
    #     # Final return cell: - best val of that partition start and all possible end

    #     n = len(arr)
    #     dp = {}

    #     def solve(start):
    #         best = 0
    #         cur_max = 0

    #         if start in dp:
    #             return dp[start]

    #         for end in range(start, min(n,start+k)):

    #             cur_max = max(cur_max, arr[end])

    #             par_len = end-start+1
    #             par_val = par_len * cur_max

    #             remaining = par_val + solve(end+1)

    #             best = max(best, remaining)
            
    #         dp[start] = best
    #         return dp[start]
    #     return solve(0)


    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        # dp[index] means: - it represents the max val that can be schieved considered i is start point
        # Which future states does it read? - it shores states from start to min(n,start+k)
        # Fill direction: - forward
        # Which variables must reset for every index? - best and cur_max
        # Final return cell: - best val of that partition start and all possible end

        n = len(arr)
        dp = [0]*(n+1)

        for start in range(n-1,-1,-1):
            best = 0
            cur_max = 0
            for end in range(start, min(n,start+k)):
                cur_max = max(cur_max, arr[end])

                par_len = end-start+1
                par_val = par_len * cur_max

                remaining = par_val + dp[end+1]

                best = max(best, remaining)
            
            dp[start] = best

        return dp[0]