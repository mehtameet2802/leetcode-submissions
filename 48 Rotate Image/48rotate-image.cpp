class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int x = matrix.size();
        for(int i=0;i<x;i++){
            for(int j=i+1;j<x;j++){
                swap(matrix[i][j],matrix[j][i]);
            }
            reverse(matrix[i].begin(),matrix[i].end());
        }
    }
};