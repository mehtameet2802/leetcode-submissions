class Solution {
public:

    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> v;
        int n = triangle.size();
        int m = triangle[n-1].size();
        for(int i=0;i<m;i++){
            v.push_back(triangle[n-1][i]);
        }
        for(int i=n-2;i>=0;i--){
            for(int j=0;j<triangle[i].size();j++){
                int m1 = triangle[i][j]+v[j];
                int m2 = triangle[i][j]+v[j+1];
                v[j] = min(m1,m2);
            }
        }
        return v[0];
    }
};