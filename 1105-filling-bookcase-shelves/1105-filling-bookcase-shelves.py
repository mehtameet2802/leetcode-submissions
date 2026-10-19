class Solution:
    # def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        
    #     n = len(books)

    #     def solve(start):
    #         if start>=n:
    #             return 0
            
    #         shelfHeight = 0
    #         width = 0
    #         answer = float('inf')

    #         for end in range(start, n):

    #             bookWidth, bookHeight = books[end]

    #             width += bookWidth

    #             if width > shelfWidth:
    #                 break
                
    #             shelfHeight = max(bookHeight, shelfHeight)

    #             answer = min(
    #                 answer, shelfHeight + solve(end+1)
    #             )
            
    #         return answer
        
    #     return solve(0)

    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        
        n = len(books)
        dp = {}

        def solve(start):
            if start>=n:
                return 0
            
            if start in dp:
                return dp[start]

            shelfHeight = 0
            width = 0
            answer = float('inf')

            for end in range(start, n):

                bookWidth, bookHeight = books[end]

                width += bookWidth

                if width > shelfWidth:
                    break
                
                shelfHeight = max(bookHeight, shelfHeight)

                answer = min(
                    answer, shelfHeight + solve(end+1)
                )
            
            dp[start] = answer
            return dp[start]
        
        return solve(0)