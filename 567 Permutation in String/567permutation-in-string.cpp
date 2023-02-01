class Solution {
public:
    
    bool checkEqual(int a[26],int b[26]){
        for(int i=0;i<26;i++){
            if(a[i]!=b[i])
                return 0;
        }
        return 1;
    }
    
    bool checkInclusion(string s1, string s2) {
        int count[26] = {0};
        int count1[26] = {0};
        for(int i=0;i<s1.length();i++){
            count[s1[i]-'a']++;
        }
        
        int i=0;
        int windowSize = s1.length();
        while(i<windowSize && i<s2.length()){
            count1[s2[i] - 'a']++;
            i++;
        }
        if(checkEqual(count,count1))
            return 1;
        
        while(i<s2.length()){
            count1[s2[i]-'a']++;
            count1[s2[i-windowSize]-'a']--;
            i++;
            if(checkEqual(count,count1))
                return 1;
        }
        return 0;
    }
};