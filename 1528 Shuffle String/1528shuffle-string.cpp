class Solution {
public:
    string restoreString(string s, vector<int>& v1) {
        vector<string> arr(s.size(),"0");
        string s1 = "";
        for(int i=0;i<s.size();i++){
            if(i == v1[i]){
                arr[i] = s[i];
            }
            else{
                arr[v1[i]] = s[i];
            }
        }
        
        for(int i=0;i<arr.size();i++){
            cout<<arr[i];
            s1 = s1 + arr[i];
        }
        
        return s1;
    }
};