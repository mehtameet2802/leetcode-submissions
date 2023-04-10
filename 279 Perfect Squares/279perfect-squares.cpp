class Solution {
public:
    int solve(vector<int> &dp,int cur){
        if(cur<=0)
            return 0;
        
        if(dp[cur]!=-1)
            return dp[cur];
        
        int ans = cur;
        for(int i=1;i*i<=cur;i++){
            int temp = i*i;
            ans = min(ans,1+solve(dp,cur-temp));
        }

        dp[cur] = ans;
        return dp[cur];
    }
    int numSquares(int n) {
        vector<int> dp(n+1,-1);
        return solve(dp,n);
    }
};