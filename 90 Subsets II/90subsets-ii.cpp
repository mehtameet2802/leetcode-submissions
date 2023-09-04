class Solution {
public:
    vector<vector<int>> ans;
    void solve(int ind,vector<int> arr,vector<int> v1){
        ans.push_back(v1);
        for(int i=ind;i<arr.size();i++){
            if(i>ind && arr[i]==arr[i-1]) continue;
            v1.push_back(arr[i]);
            solve(i+1,arr,v1);
            v1.pop_back();
        }

    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());  
        solve(0,nums,{});
        return ans;
    }
};