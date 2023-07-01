#include<bits/stdc++.h>
class Solution {
public:
    
    int convert(char a){
        return a-'0';
    }
    
    string addStrings(string num1, string num2) {
        string result = "";
        int i = num1.size()-1;
        int j = num2.size()-1;
        int carry = 0;
        while(i>=0 || j>=0){
            int sum = carry;
            if(i>=0){
                sum = sum+convert(num1[i]);
                // cout<<sum<<"\n";
            }
            if(j>=0){
                sum = sum+convert(num2[j]);
                // cout<<sum<<"\n";
            }
            carry = sum/10;
            result = result+to_string(sum%10);
            i--;
            j--;
        }
        if(carry!=0){
            result = result+to_string(carry);
        }
        reverse(result.begin(),result.end());
        return result;
    }
};