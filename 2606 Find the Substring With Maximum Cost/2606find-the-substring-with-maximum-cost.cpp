class Solution {
public:
    
    void solve(vector<int> cost,vector<int>&dp,int n){
        dp[n] = cost[n];
        
        for(int i=n-1;i>=0;i--){
            int y = cost[i]+dp[i+1];
            dp[i] = max(cost[i],y);
        }
    } 
    
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        map<char,int> mp;
        for(int i=0;i<chars.size();i++){
            mp[chars[i]] = vals[i];
        }
        
        vector<int> dp(s.size(),-1);
        vector<int> cost(s.size(),-1);
        for(int i=0;i<s.size();i++){
            if(mp.find(s[i])==mp.end())
                cost[i] = (int)(s[i]-'a')+1;
            else
                cost[i] = mp[s[i]];
        }
        solve(cost,dp,s.size()-1);
        
        int ans=0;
        for(int i=0;i<dp.size();i++){
            ans = max(ans,dp[i]);
        }
        return ans;
        
        
    }
};