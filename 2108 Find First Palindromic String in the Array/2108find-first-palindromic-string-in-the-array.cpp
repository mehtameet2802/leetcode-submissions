class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(int i=0;i<words.size();i++){
            int count = 0;
            for(int j=0;j<words[i].size()/2;j++){
                int n = words[i].size();
                if(words[i][j] == words[i][n-j-1]){
                    count++;
                }
            }
            if(count == words[i].size()/2){
                return words[i];
            }
        }
        return "";
    }
};