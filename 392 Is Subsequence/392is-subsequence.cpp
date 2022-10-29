class Solution {
public:
    bool isSubsequence(string s, string t) {
        int p1 = 0;
        int p2 = 0;
        while(p1!=t.size()){
            if(p2 == s.size())
                return true;
            if(s[p2] == t[p1])
                p2++;
            p1++;
        }
        if(p2 == s.size())
            return true;
        return false;
    }
};