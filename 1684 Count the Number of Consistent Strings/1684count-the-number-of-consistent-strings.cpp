class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int f =0;
        for(int i=0;i<words.size();i++){
            int count = 0;
            for(int j=0;j<words[i].size();j++){
                if(allowed.find(words[i][j]) == -1){
                    // cout<<words[i][j];
                    // cout<<count;
                    count++;
                }
            }
            if(count!=0){
                f++;
            }
        }
        return words.size()-f;
    }
};