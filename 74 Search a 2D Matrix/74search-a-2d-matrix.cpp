class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mat, int target) {
        int r = mat.size();
        int c = mat[0].size();
        int s = 0;
        int e = r*c-1;
        while(s<=e){
            int mid = s+(e-s)/2;
            if(mat[mid/c][mid%c] == target)
                return true;
            else if(mat[mid/c][mid%c]<target)
                s = mid+1;
            else
                e = mid-1;
        }
        return false;
    }
};