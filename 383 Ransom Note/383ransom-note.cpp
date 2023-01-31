class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char,int> mp1;
        map<char,int> mp2;
        
        for(int i=0;i<ransomNote.size();i++){
            mp1[ransomNote[i]]++;
        }
        for(int i=0;i<magazine.size();i++){
            mp2[magazine[i]]++;
        }

        for(auto it:mp1){
            auto it1 = mp2.find(it.first);
            if(it1 == mp2.end() || it1->second<it.second)
                return false;
        }
        return true;
    }
};