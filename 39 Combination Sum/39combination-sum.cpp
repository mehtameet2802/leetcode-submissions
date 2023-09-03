class Solution {
public:
    set<vector<int>> ans;
    void solve(vector<int> v1,vector<int> arr,int target,int cur,int index){
        if(cur==target){
            sort(v1.begin(),v1.end());
            ans.insert(v1);
            return;
        }

        if(cur>target)
            return;

        for(int i=index;i<arr.size();i++){
            v1.push_back(arr[i]);
            solve(v1,arr,target,cur+arr[i],i);
            v1.pop_back();
        }
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> v1;

        for(int i=0;i<candidates.size();i++){
            solve({candidates[i]},candidates,target,candidates[i],i);
        }

        for(auto it:ans){
            v1.push_back(it);
        }
        return v1;
    }
};