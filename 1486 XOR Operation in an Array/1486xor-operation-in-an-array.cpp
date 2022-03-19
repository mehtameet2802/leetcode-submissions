class Solution {
public:
    int xorOperation(int n, int start) {
        vector<int> v1;
        for(int i=0;i<n;i++){
            int x = start + i*2;
            v1.push_back(x);
        }
        for(int i=0;i<v1.size()-1;i++){
            v1[0] = v1[0]^v1[i+1];
        }
        return v1[0];
    }
};