class Solution {
public:
    bool isPalindrome(int s,int e,string s1){
        while(s<=e){
            if(s1[s]!=s1[e])
                return false;
            s++;
            e--;
        }
        return true;
    }

    void solve(int start,string s1,vector<string> &v1,vector<vector<string>> &ans){
        if(start>=s1.size()){
            ans.push_back(v1);
            return;
        }

        for(int i=start;i<s1.size();i++){
            if(isPalindrome(start,i,s1)){
                v1.push_back(s1.substr(start,i-start+1));
                solve(i+1,s1,v1,ans);
                v1.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> ans;
        vector<string> v1;
        solve(0,s,v1,ans);
        return ans;
    }
};