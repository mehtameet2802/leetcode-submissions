class Solution {
public:
    
    string reverseStr(string st){
        int s = 0;
        int e = st.length()-1;
        while(s<=e){
            swap(st[s],st[e]);
            s++;
            e--;
        }
        return st;
    }
    
    bool isValid(char c){
        if((c>='A' && c<='Z') || (c>='a' && c<='z') || (c>='0' && c<='9')){
            return 1;
        }else{
            return 0;
        }
    }
    
    char tolowerCase(char c){
        if(c>='A' && c<='Z'){
            return c-'A'+'a';
        }else{
            return c;
        }
    }
    
    bool isPalindrome(string s) {
        string temp = "";
        for(int i=0;i<s.length();i++){
            if(isValid(s[i])){
                temp += s[i];
            }
        }
        
        for(int i=0;i<temp.length();i++){
            temp[i] = tolowerCase(temp[i]);
        }
        string temp1 = reverseStr(temp);
        
        cout<<temp;
        if(temp == temp1){
            return 1;
        }else{
            return 0;
        }
    }
};