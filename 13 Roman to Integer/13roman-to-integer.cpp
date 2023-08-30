class Solution {
public:
    int romanToInt(string s) {
        map<char,int> mp;
        mp['I'] = 1;
        mp['V'] = 5;
        mp['X'] = 10;
        mp['L'] = 50;
        mp['C'] = 100;
        mp['D'] = 500;
        mp['M'] = 1000;
        int ans = 0;
        for(int i=s.size()-1;i>=0;i--){
            if(i==0)
                ans+=mp[s[i]];
            else if(s[i]=='V' && s[i-1]=='I'){
                ans+=4;
                i--;
            }
            else if(s[i]=='X' && s[i-1]=='I'){
                ans+=9;
                i--;
            }
            else if(s[i]=='L' && s[i-1]=='X'){
                ans+=40;
                i--;
            }
            else if(s[i]=='C' && s[i-1]=='X'){
                ans+=90;
                i--;   
            }
            else if(s[i]=='D' && s[i-1]=='C'){
                ans+=400;
                i--;
            }
            else if(s[i]=='M' && s[i-1]=='C'){
                ans+=900;
                i--;
            }
            else
                ans+=mp[s[i]];
        }
        return ans;
    }
};