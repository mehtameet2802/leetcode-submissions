#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        vector<int> v1 = nums;
        vector<int> v2 = nums;
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end(),greater<int>());
        if(v1 == nums || v2==nums){
            return 1;
        }
        return 0;
    }
};