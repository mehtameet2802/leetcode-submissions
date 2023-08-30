class Solution {
public:
    int beautySum(string s) {
        int ans = 0;
        for(int i=0;i<s.size();i++){
            map<char,int> mp;
            for(int j=i;j<s.size();j++){
                mp[s[j]]+=1;
                int m1 = INT_MIN;
                int m2 = INT_MAX;
                for(auto it:mp){
                    m1 = max(m1,it.second);
                    m2 = min(m2,it.second);
                }
                ans+=(m1-m2);
            }
        }
        return ans;
    }
};