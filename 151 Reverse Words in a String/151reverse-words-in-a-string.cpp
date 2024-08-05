class Solution {
public:
    string reverseWords(string s) {
        vector<string> v1;
        string s1 = "";
        for(int i=0;i<s.size();i++){
            if(s[i]==' ' && s1.length()==0)
                continue;
            else if(s[i]==' ' && s1.length()>0){
                v1.push_back(s1);
                s1 = "";
            }
            else
                s1+=s[i];
        }
        if(s1!="")
            v1.push_back(s1);
        
        reverse(v1.begin(),v1.end());

        string ans = "";
        for(int i=0;i<v1.size();i++){
            ans+=v1[i];
            if(i!=v1.size()-1)
                ans+=' ';
        }        
        return ans;

    }
};