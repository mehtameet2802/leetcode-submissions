class Solution {
public:
    // bool check(vector<int> v,vector<int> nums){
    //     for(int i=0;i<v.size();i++){
    //         if(v[i]!=nums[i])
    //             return false;
    //     }
    //     return true;
    // }

    // void perm(int index,vector<int> &v,vector<int> nums,vector<vector<int>> &ans){
    //     if(index>=nums.size()){
    //         ans.push_back(v);
    //         return;
    //     }

    //     perm(index+1,v,nums,ans);

    //     int ele = nums[index];
    //     v.push_back(ele);
    //     perm(index+1,v,nums,ans);

    // }
    void nextPermutation(vector<int>& nums) {
        // vector<int> v;
        // vector<vector<int>> ans;
        // perm(0,v,nums,ans);
        // sort(ans.begin(),ans.end());
        // for(int i=0;i<ans.size();i++){
        //     if(ans[i].size() == nums.size()){
        //         cout<<"here1";
        //         if(check(ans[i],nums)){
        //             cout<<"here2";
        //             if(i == ans.size()-1)
        //                 v = ans[i+1];
        //             else
        //                 v = ans[i];
        //             cout<<"here3";
        //             break;
        //         }
        //     }
        // }
        // nums = v;
        next_permutation(nums.begin(),nums.end());
    }
};