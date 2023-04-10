#include<bits/stdc++.h>
class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> mp;
        for(int i=0;i<nums1.size();i++){
            mp[nums1[i]]++;
        }
        for(int i=0;i<nums2.size();i++){
            mp[nums2[i]]++;
        }
        
        for(auto it:mp){
            if(it.second==2)
                return it.first;
        }
        
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int x = min(nums1[0],nums2[0]);
        x=x*10;
        x+=max(nums1[0],nums2[0]);
        return x;
    }
};