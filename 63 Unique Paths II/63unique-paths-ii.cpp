class Solution {
public:

    int solve(int sx,int sy,int dx,int dy,vector<vector<int>> &dp){
        if(sx==0 && sy==0)
            return 1;
        
        if(sx<0 || sy<0)
            return 0;
        
        if(dp[sx][sy]!=-1)
            return dp[sx][sy];
        
        int ans = 0;
        if(sx-1>=0 && sx<=dx && sy>=0 && sy<=dy && dp[sx-1][sy]!=-2){
            ans+=solve(sx-1,sy,dx,dy,dp);
        }
        if(sy-1>=0 && sy<=dy && sx>=0 && sx<=dx && dp[sx][sy-1]!=-2){
            ans+=solve(sx,sy-1,dx,dy,dp);
        }
        dp[sx][sy] = ans;
        return dp[sx][sy];
    }
    
    int uniquePathsWithObstacles(vector<vector<int>>& dp) {
        int ans = 0;
        int m = dp.size();
        int n = dp[0].size();
        if(dp[0][0] == 1 || dp[m-1][n-1] == 1)
            return ans;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(dp[i][j]==0)
                    dp[i][j] = -1;
                if(dp[i][j] == 1)
                    dp[i][j] = -2;
            }
        }
        ans = solve(m-1,n-1,m-1,n-1,dp);
        return ans;
    }
};