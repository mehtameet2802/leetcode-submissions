class Solution {
public:

    int solve(int n,int m,vector<vector<int>> dp){
        if(n==m)
            return 1;
        if(m==0)
            return 1;
        
        if(dp[n][m]!=-1)
            return dp[n][m];
        
        dp[n][m] = solve(n-1,m,dp)+solve(n-1,m-1,dp);
        return dp[n][m];
    }

    vector<int> getRow(int n) {
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        for(int i=0;i<=n;i++){
            for(int j=0;j<=i;j++){
                if(i==j){
                    dp[i][j] = 1;
                    continue;
                }
                if(j==0){
                    dp[i][j] = 1;
                    continue;
                }                

                dp[i][j] = dp[i-1][j]+dp[i-1][j-1];
            }
        }
        // int ans = solve(n,n,dp);
        return dp[n];
    }
};