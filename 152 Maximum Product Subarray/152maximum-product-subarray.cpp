class Solution {
public:

    void solve(vector<int>&dp1,int n,vector<int>& nums,vector<int>&dp2){
        dp1[n] = nums[n];
        dp2[n] = nums[n];
        for(int i=n-1;i>=0;i--){
            int x = nums[i]*dp1[i+1];
            int y = nums[i]*dp2[i+1];
            dp1[i] = max(x,max(y,nums[i]));
            dp2[i] = min(x,min(y,nums[i]));
        }
    }

    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp1(n,-1);
        vector<int> dp2(n,-1);
        solve(dp1,n-1,nums,dp2);
        int ans = INT_MIN;
        for(int i=0;i<n;i++){
            ans = max(ans,max(dp1[i],dp2[i]));
        }
        return ans;
    }
};