class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string ans = strs[0];
        for(int i=1;i<strs.size();i++){
            string s1 = "";
            for(int j=0;j<ans.size();j++){
                if(strs[i][j] == ans[j])
                    s1+=ans[j];
                else if(ans[j]!=strs[i][j] && s1.length()==0)
                    return "";
                else
                    break;
            }
            ans = s1;
        }
        return ans;
    }
};