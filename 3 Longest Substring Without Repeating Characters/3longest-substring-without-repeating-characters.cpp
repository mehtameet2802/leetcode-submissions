class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        int len = INT_MIN;
        if(s.size()==0 || s.size()==1)
            return s.size();
        map<char,int> mp;
        for(right;right<s.size();right++){
            if(mp.find(s[right])!=mp.end()){
                int z = mp[s[right]];
                if(z>=left)
                    left = z+1;
            }
            mp[s[right]] = right;
            len = max(len,right-left+1);
        }
        return len;
    }
};