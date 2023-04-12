class Solution {
public:
    int solve1(int sx,int sy,int dx,int dy,vector<vector<int>> &dp){
        if(sx==0 && sy==0)
            return 1;
        
        if(sx<0 || sy<0)
            return 0;
        
        if(dp[sx][sy]!=-1)
            return dp[sx][sy];
        
        int ans = 0;
        if(sx-1>=0 && sx<=dx && sy>=0 && sy<=dy){
            ans+=solve1(sx-1,sy,dx,dy,dp);
        }
        if(sy-1>=0 && sy<=dy && sx>=0 && sx<=dx){
            ans+=solve1(sx,sy-1,dx,dy,dp);
        }
        dp[sx][sy] = ans;
        return dp[sx][sy];
    }


    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m,vector<int>(n,-1));
        return solve1(m-1,n-1,m-1,n-1,dp);
    }
};