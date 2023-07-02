class Solution {
public:


    string check(int n){
        if(n == 1)
            return "1";
        
        if(n == 2)
            return "11";
        
        string str = check(n-1);
        string index = "";
        vector<int> v1;
        vector<char> v2;

        
        int i=0;
        while(i<str.length()){
            int j=i;
            int count=0;
            while(str[j] == str[i]){
                count++;
                j++;
            }
            v2.push_back(str[i]);
            v1.push_back(count);
            i=j;
        }

        string ans = "";
        for(int k=0;k<v1.size();k++){
            ans+=to_string(v1[k]);
            ans+=v2[k];
        }
        return ans;
    }

    string countAndSay(int n) {
        return check(n);
    }
};