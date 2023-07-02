#include<bits/stdc++.h>
class Solution {
public:
    int compareVersion(string version1, string version2) {
        map<int,int> mp1;
        map<int,int> mp2;
        int x1 = version1.length();
        int x2 = version2.length();
        int ans = 0;
        int index1 = 0;
        for(int i=0;i<x1;i++){
            if(version1[i] == '.'){
                mp1[index1] = ans;
                ans = 0;
                index1++;
            }
            else{
                ans = ans*10;
                ans+=version1[i]-'0';
            }
        }
        mp1[index1] = ans;
        index1++;
        
        
        ans = 0;
        int index2 = 0;
        for(int i=0;i<x2;i++){
            if(version2[i] == '.'){
                mp2[index2] = ans;
                ans = 0;
                index2++;
            }
            else{
                ans = ans*10;
                ans+=version2[i]-'0';
            }
        }
        mp2[index2] = ans;
        index2++;


        if(index1 < index2){
            while(index1<index2){
                mp1[index1] = 0;
                index1++;
            }
        }

        if(index2<index1){
            while(index2<index1){
                mp2[index2] = 0;
                index2++;
            }
        }

        auto it1 = mp1.begin();
        auto it2 = mp2.begin();

        while(it1!=mp1.end() && it2!=mp2.end()){
            if(it1->second < it2->second)
                return -1;
            else if(it2->second<it1->second)
                return 1;
            it1++;
            it2++;
        }
        return 0;
    }
};