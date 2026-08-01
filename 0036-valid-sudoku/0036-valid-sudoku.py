from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        
        board_map = defaultdict(set)
        r_map = defaultdict(set)
        c_map = defaultdict(set)


        for i in range(ROWS):
            for j in range(COLS):
                ele = board[i][j]
                if ele == ".":
                    continue

                if ele in r_map[i] or ele in c_map[j] or ele in board_map[(i//3,j//3)]:
                    return False
                
                r_map[i].add(ele)
                c_map[j].add(ele)
                board_map[(i//3,j//3)].add(ele)
        
        return True


                                             