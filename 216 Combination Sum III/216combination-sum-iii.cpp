class Solution {
public:
    vector<vector<int>> ans;
    void solve(int n, int k,int ind,vector<int> v1){
        if(n==0 && k==v1.size()){
            ans.push_back(v1);
            return;
        }
        
        for(int i=ind;i<=9;i++){
            v1.push_back(i);
            solve(n-i,k,i+1,v1);
            v1.pop_back();
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        solve(n,k,1,{});
        return ans;
    }
};