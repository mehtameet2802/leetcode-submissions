class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1,-1);
        for(int i=0;i<=n;i++){
            if(i==0){
                dp[i] =0;
                continue;
            }
            int x = i;
            int count = 0;
            while(x!=0){
                count += x&1;
                x = x>>1;
                if(dp[x]!=-1){
                    count+=dp[x];
                    x = 0;
                }
            }
            dp[i] = count;
        }
        return dp;
    }
};