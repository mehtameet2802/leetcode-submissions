class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> v1;
        v1.push_back({1});
        if(numRows==1)
            return v1;
        v1.push_back({1,1});
        for(int i=2;i<numRows;i++){
            vector<int> v = {1};
            for(int j=1;j<i;j++){
                v.push_back(v1[i-1][j-1]+v1[i-1][j]);
            }
            v.push_back(1);
            v1.push_back(v);
        }
        return v1;
    }
};