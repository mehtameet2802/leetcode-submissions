class Solution {
public:
    int solve(vector<int> &nums,int cur,vector<int>&dp){
        if(cur == nums.size()-1)
            return nums[cur];
    
        if(cur>=nums.size())
            return 0;
    
        if(dp[cur]!=-1)
            return dp[cur];
    
        int inc = nums[cur]+solve(nums,cur+2,dp);
        int exc = solve(nums,cur+1,dp);

        dp[cur] = max(inc,exc);
        return dp[cur];
    }
    
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(),-1);
        return solve(nums,0,dp);
    }
};