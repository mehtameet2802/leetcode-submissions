class Solution {
public:
    void perm(int index,string str,string v,set<string>&ans,int k){
        if(index>=k){
            ans.insert(str);
            return;
        }

        // include cap
        char c1 = toupper(v[index]);
        perm(index+1,str+c1,v,ans,k);

        // include low
        c1 = tolower(v[index]);
        perm(index+1,str+c1,v,ans,k);
    }
    vector<string> letterCasePermutation(string s) {
        set<string> a;
        vector<string> ans;
        perm(0,"",s,a,s.size());
        for(auto it:a){
            ans.push_back(it);
        }
        return ans;
    }
};