class Solution {
public:
    int balancedStringSplit(string s) {
        int cL = 0;
        int cR = 0;
        int cS = 0;
        for(int i = 0;s[i]!='\0';i++){
            if(s[i] == 'R'){
                cR++;
            }
            if(s[i] == 'L'){
                cL++;
            }
            if(cL == cR){
                cS++;
                cL = 0;
                cR = 0;
            }
        }
        cout<<cS;
        return cS;
    }
};