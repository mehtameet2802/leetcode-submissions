// class Solution {
// public:
//     bool isValidSudoku(vector<vector<char>>& board) {

//         for(int i=0;i<9;i++){
//             map<char,int> row;
//             for(int j=0;j<9;j++){
//                 row[board[i][j]]++;
//                 if(board[i][j]!='.' && row[board[i][j]]>1)
//                     return false;
//             }
//         }

//         for(int i=0;i<9;i++){
//             map<char,int> col;
//             for(int j=0;j<9;j++){
//                 col[board[j][i]]++;
//                 if(board[j][i]!='.' && col[board[j][i]]>1)
//                     return false;
//             }
//         }
//         return true;

//     }
// };

class Solution {
public:
    /* test a submatrix */
    bool test(int sr, int sc, int er, int ec, vector<vector<char>>& b)
    {
        unsigned char map[10] = { 0 };        
        for (int r = sr; r <= er; r++) {
            for (int c = sc; c <= ec; c++) {
                int v = (int)b[r][c] - '0';
                if (v < 10 && v >= 0) {
                    if (map[v] >= 1) return false;   // occurs more than once
                    map[v]++;
                }
            }
        }
        return true;
    }
    
    bool isValidSudoku(vector<vector<char>>& b) {
        int rows = b.size(), cols = b[0].size();
        
        for (int r = 0; r < rows; r++) if (!test(r, 0, r, cols-1, b)) return 0;
        for (int c = 0; c < cols; c++) if (!test(0, c, rows-1, c, b)) return 0;
        for (int r = 0; r < rows; r += 3) {
            for (int c = 0; c < cols; c += 3) {
                if (!test(r, c, r+2, c+2, b)) return 0;
            }
        }
        return true;
    }
};
