class Solution {
public:
    string frequencySort(string s) {
        vector<pair<int,char>> v1('z'+1,{0,'0'});
        for(int i=0;i<s.size();i++){
            v1[s[i]] = {v1[s[i]].first+1,s[i]};
        }

        sort(v1.begin(),v1.end());
        string ans = "";
        for(int i=0;i<v1.size();i++){
            ans = string(v1[i].first,v1[i].second)+ans;
        }
        return ans;
    }
};