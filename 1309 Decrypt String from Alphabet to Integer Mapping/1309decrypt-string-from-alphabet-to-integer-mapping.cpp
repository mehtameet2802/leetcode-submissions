#include<bits/stdc++.h>
class Solution {
public:
    string freqAlphabets(string s) {
        string s1 = "";
        int i=0;
        while(s[i]!='\0'){
            string s2 = "";
            if(s[i] == '#'){
                i++;
                continue;
            }
            if(s[i+1] && s[i+2] && s[i+2] == '#'){
                s2 = s2+s[i]+s[i+1];
                i+=2;
            }
            else{
                s2 = s2+s[i];
                i++;
            }
            int s3 = stoi(s2);
            cout<<char(s3+96);
            s1 = s1+ char(s3+96);
            // cout<<s1;
        }
        cout<<s1;
        return s1;
    }
};