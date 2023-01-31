class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> v1(26,-1);
        vector<int> v2(26,-1);
        for(int i=0;i<s.size();i++){
            if(v1[s[i]-97] == -1){
                v1[s[i]-97] = 1;
                v2[s[i]-97] = i;
            }
            else{
                v1[s[i]-97] = v1[s[i]-97]+1;
            }
        }

        // for(int i=0;i<26;i++){
        //     cout<<v1[i];
        // }
        // cout<<endl;
        // for(int i=0;i<26;i++){
        //     cout<<v2[i];
        // }

        char c;
        int index = INT_MAX; 
        for(int i=0;i<26;i++){
            if(v1[i]==1){
                index = min(index,v2[i]);
            }
        }
        if(index == INT_MAX)
            return -1;
        return index;
    }
};