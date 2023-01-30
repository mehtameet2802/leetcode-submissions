class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int s = mat.size();
        int e = mat[0].size();
        int count = s*e;
        int r1 = r;
        int c1 = c;
        if(count == r1*c1){
            vector<int> num;
            for(int i=0;i<s;i++){
                for(int j=0;j<e;j++){
                    num.push_back(mat[i][j]);
                }
            }
            vector<vector<int>> ans;
            int j=0;
            while(r1>0){
                vector<int> a;
                while(j<c1){
                    a.push_back(num[j]);
                    j++;
                }
                c1+=c;
                r1--;
                ans.push_back(a);
            }
            return ans;
        }
        return mat;
        
    }
};