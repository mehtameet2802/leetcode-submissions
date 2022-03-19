class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& w1, vector<string>& w2) {
        string s1 = "";
        string s2 = "";
        for(int i =0;i<w1.size();i++){
            s1 = s1+w1[i];
        }
        for(int j=0;j<w2.size();j++){
            s2 = s2+w2[j];
        }
        if(s2 == s1){
            return 1;
        }
        return 0;
    }
};