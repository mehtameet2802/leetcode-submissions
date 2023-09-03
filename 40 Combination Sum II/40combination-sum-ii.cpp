class Solution {
public:
    vector<vector<int>> ans;
    void solve(int ind,int tar,vector<int> arr,vector<int> v1){
        if(tar==0){
            ans.push_back(v1);
            return;
        }

        for(int i=ind;i<arr.size();i++){
            if(i>ind && arr[i]==arr[i-1]) continue;
            if(arr[i]>tar) break;
            v1.push_back(arr[i]);
            solve(i+1,tar-arr[i],arr,v1);
            v1.pop_back();
        }

    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
      sort(candidates.begin(),candidates.end());  
      vector<int> v1;
      solve(0,target,candidates,v1);
      return ans;
    }
};