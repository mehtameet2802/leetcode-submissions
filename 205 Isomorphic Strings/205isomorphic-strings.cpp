class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char,char> mp;
        map<char,char> mp1;
        if(s.size()!=t.size())
            return false;
        
        for(int i=0;i<s.length();i++){
            if(mp.find(s[i])==mp.end()){
                mp[s[i]] = t[i];
                if(mp1.find(t[i])==mp1.end())
                    mp1[t[i]] = s[i];
                else if(mp1[t[i]]!=s[i])
                    return false;
            }
            else{
                if(mp[s[i]] != t[i])
                    return false;
                
                if(mp1[t[i]]!=s[i])
                    return false;
            }
        }
        return true;
    }
};