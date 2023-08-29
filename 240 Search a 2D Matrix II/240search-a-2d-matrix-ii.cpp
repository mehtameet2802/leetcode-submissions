class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mat, int target) {
        int r = mat.size();
        int c = mat[0].size()-1;
        int r1 = 0;
        while(r1<r && c>=0){
            if(mat[r1][c]==target)
                return true;
            else if(mat[r1][c]>target)
                c--;
            else
                r1++;
        }
        return false;
    }
};